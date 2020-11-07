import cv2
from utils.py_tools import EventHook

WIN_NAME = "Video"

on_point_selected = EventHook()

def select_point(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        on_point_selected.fire(x, y)

cv2.namedWindow(WIN_NAME)
cv2.setMouseCallback(WIN_NAME, select_point)

def show(frame):
    cv2.imshow(WIN_NAME, frame)
    cv2.waitKey(1)