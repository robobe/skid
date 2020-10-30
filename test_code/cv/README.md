

# OpenCV Gstreamer writer
- create virtual camera loopback

[v4l2loopback](https://github.com/umlaeute/v4l2loopback)

> Build from source, repository version allow open device as read only !!!
```bash
# video_nr: device number
sudo modprobe v4l2loopback
```

## usage
```bash
gst-launch-1.0 v4l2src device=/dev/video2 \
! video/x-raw, width=640,height=480,framerate=20/1 \
! videoconvert \
! v4l2sink device=/dev/video4

# Test Source
gst-launch-1.0 videotestsrc ! v4l2sink device=/dev/video4

# Read
gst-launch-1.0 -vv v4l2src device=/dev/video4  ! autovideosink
```

## 