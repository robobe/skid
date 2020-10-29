
# Gstreamer RAW Stream
## Tx
```
gst-launch-1.0 -v videotestsrc \
! rtpvrawpay \
! udpsink host="127.0.0.1" port="5000"
```

## Rx
```
gst-launch-1.0 udpsrc port="5000" caps = "application/x-rtp, media=(string)video, clock-rate=(int)90000, encoding-name=(string)RAW, sampling=(string)YCbCr-4:2:0, depth=(string)8, width=(string)320, height=(string)240, colorimetry=(string)BT601-5, payload=(int)96, ssrc=(uint)1103043224, timestamp-offset=(uint)1948293153, seqnum-offset=(uint)27904" \
! rtpvrawdepay \
! videoconvert \
! queue \
! xvimagesink sync=false
```