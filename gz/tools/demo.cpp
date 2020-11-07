#include <vector>
#include <stdio.h>
#include <fcntl.h>
#include <errno.h>
#include <unistd.h>
#include <iostream>
#include <cassert>
#include <algorithm>
#include <sys/ioctl.h>
#include <linux/videodev2.h>

#include <CImg.h>

#define VIDEO_OUT "/dev/video4" // V4L2 Loopack

#define WIDTH  640
#define HEIGHT 480

int main() {
    using namespace cimg_library;

    CImg<uint8_t> canvas(WIDTH, HEIGHT, 1, 3);
    const uint8_t red[] = {255, 0, 0};
    const uint8_t blue[] = {0, 0, 255};

    int fd;
    if ((fd = open(VIDEO_OUT, O_WRONLY | O_SYNC)) == -1) {
      std::cerr << "Unable to open video output!\n";
      return 1;
    }

    int width = canvas.width(), height = canvas.height();
    struct v4l2_format vid_format;
    vid_format.type = V4L2_BUF_TYPE_VIDEO_OUTPUT;
    vid_format.fmt.pix.pixelformat  = V4L2_PIX_FMT_YUYV;
    vid_format.fmt.pix.width        = width;
    vid_format.fmt.pix.height       = height;
    vid_format.fmt.pix.field        = V4L2_FIELD_NONE;
    vid_format.fmt.pix.bytesperline = width * 2;
    vid_format.fmt.pix.sizeimage    = width * height * 2;
    vid_format.fmt.pix.colorspace   = V4L2_COLORSPACE_JPEG;

    if (ioctl(fd, VIDIOC_S_FMT, &vid_format) == -1) {
      std::cerr << "Unable to set video format! Errno: " << errno << '\n';
      return 1;
    }

    std::vector<uint8_t> buffer;
    buffer.resize(vid_format.fmt.pix.sizeimage);

    std::cout << "Stream running!\n";

    while (true) {
      canvas.draw_plasma();
      // canvas.draw_rectangle(
      //   0, 0, width, height, red, 1);
      canvas.draw_text(5,5, "Hello World!", blue);
      canvas.draw_text(5, 20, "Image freshly rendered with the CImg Library!", red);

      bool skip = true;
      cimg_forXY(canvas, cx, cy) {
        size_t row = cy * width * 2;
        uint8_t r, g, b, y;
        r = canvas(cx, cy, 0);
        g = canvas(cx, cy, 1);
        b = canvas(cx, cy, 2);

        y = std::clamp<uint8_t>(r * .299000 + g * .587000 + b * .114000, 0, 255);
        buffer[row + cx * 2] = y;
        if (!skip) {
          uint8_t u, v;
          u = std::clamp<uint8_t>(r * -.168736 + g * -.331264 + b * .500000 + 128, 0, 255);
          v = std::clamp<uint8_t>(r * .500000 + g * -.418688 + b * -.081312 + 128, 0, 255);
          buffer[row + (cx - 1) * 2 + 1] = u;
          buffer[row + (cx - 1) * 2 + 3] = v;
        }
        skip = !skip;
      }

      write(fd, buffer.data(), buffer.size());
    }
}
