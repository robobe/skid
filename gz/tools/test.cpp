#include "opencv2/opencv.hpp"
#include <iostream>
#include "image_converter.hpp"
#include "spdlog/spdlog.h"
#include "spdlog/sinks/stdout_color_sinks.h"
#include <sys/ioctl.h>

namespace spd = spdlog;
using namespace std;
using namespace cv;

int main()
{
    int ret_code = -1;
    auto console = spd::stdout_color_mt("console");
    auto log = spd::get("console");
    log->info("App start");
    struct v4l2_capability vid_caps;
    ImageConverter ic(640, 480, "YUYV");
    VideoCapture cap("/dev/video2");
    int fdwr = open("/dev/video4", O_RDWR);
    ret_code = ioctl(fdwr, VIDIOC_QUERYCAP, &vid_caps);
    auto vid_format = ic.format();
    ret_code = ioctl(fdwr, VIDIOC_S_FMT, &vid_format);
    if (ret_code == -1)
    {
            log->error("Video format failed");
    }
    std::vector<unsigned char> out_buffer;
    int size = 640 * 480 * 2;
    out_buffer.resize(size);
    // Check if camera opened successfully
    if (!cap.isOpened())
    {
        cout << "Error opening video stream or file" << endl;
        return -1;
    }

    while (1)
    {

        Mat frame;
        cap >> frame;

        // If the frame is empty, break immediately
        if (frame.empty())
            break;
        ic.fmt_yuyv(frame, out_buffer);
        write(fdwr, out_buffer.data(), out_buffer.size());
        imshow("Frame", frame);
        char c = (char)waitKey(25);
        if (c == 27)
            break;
    }

    cap.release();
    close(fdwr);
    destroyAllWindows();
    return 0;
}
