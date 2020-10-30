

## usage
```
gst-launch-1.0 -v udpsrc port=5600 \
! application/x-rtp, encoding-name=H264,payload=96 \
! rtph264depay \
! avdec_h264 ! \
 autovideosink sync=false
```

```
gst-launch-1.0 -v udpsrc port=5600 \
! application/x-rtp, encoding-name=H264,payload=96 \
! rtph264depay \
! avdec_h264 \
! v4l2sink device=/dev/video4
 
```