

# Install
```
pip install -U pip wheel setuptools
pip install -r requirements.txt
```

# Gazebo
Sources
gst_plugin from: PX4
ardupilot plugin from:


# Video
- check h264 from gst_camera_plugin

```
gst-launch-1.0 -v udpsrc port=5600 \
! application/x-rtp, encoding-name=H264,payload=96 \
! rtph264depay \
! avdec_h264 ! \
 autovideosink sync=false
```