import cv2
import sys
import numpy as np

in_pipe = "udpsrc port=5000 \
    ! application/x-rtp,media=video,payload=26,clock-rate=90000,encoding-name=JPEG,framerate=20/1 \
    ! rtpjpegdepay \
    ! jpegdec \
    ! videoconvert \
    ! appsink"

video = cv2.VideoCapture(in_pipe, cv2.CAP_GSTREAMER)

# Exit if video not opened.
if not video.isOpened():
    print ("Could not open video")
    sys.exit()

# Read first frame.
ok, frame = video.read()
if not ok:
    print ('Cannot read video file')
    sys.exit()

old_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
lk_params = dict(winSize = (15, 15),
                 maxLevel = 4,
                 criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))
x, y, w, h = cv2.selectROI(frame, False)
point_selected = True
old_points = np.array([[x, y]], dtype=np.float32)

while True:
    _, frame = video.read()
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    if point_selected is True:
        # cv2.circle(frame, point, 5, (0, 0, 255), 2)

        new_points, status, error = cv2.calcOpticalFlowPyrLK(old_gray, 
            gray_frame, 
            old_points, 
            None, 
            **lk_params)
        old_gray = gray_frame.copy()
        old_points = new_points
        x, y = new_points.ravel()
        cv2.circle(frame, (int(x), int(y)), 5, (0, 255, 0), -1)
        cv2.putText(frame, str(error[0][0]), (100,20), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50,170,50),2)
        cv2.putText(frame, str(status), (100,40), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50,170,50),2)


    cv2.imshow("Frame", frame)

    key = cv2.waitKey(1)
    if key == 27:
        break

video.release()
cv2.destroyAllWindows()