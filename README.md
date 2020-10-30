

# Install
```
pip install -U pip wheel setuptools
pip install -r requirements.txt
```

# source codes 
- [gst_camera_plugin](https://github.com/PX4/PX4-SITL_gazebo/tree/06e801fe8b5267e561f00d8847a6343cb2386ab6/src)
- [ardupilot gazebo plugin (plug)](https://github.com/khancyr/ardupilot_gazebo)
- [ardupilot gazebo plugin (model and world)](https://github.com/SwiftGust/ardupilot_gazebo)
- [Intel gazebo-realsense](https://github.com/intel/gazebo-realsense)
  - > Must compile with c++17 flag on ubuntu 20.04


# Video
- check h264 from gst_camera_plugin

```
gst-launch-1.0 -v udpsrc port=5600 \
! application/x-rtp, encoding-name=H264,payload=96 \
! rtph264depay \
! avdec_h264 ! \
 autovideosink sync=false
```