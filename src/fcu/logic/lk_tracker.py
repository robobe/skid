import cv2
import numpy as np
import logging
from utils.py_tools import EventHook

log = logging.getLogger(__name__)

class lk():
    def __init__(self, name="lk"):
        self.__name = name
        self.__old_frame = None
        self.__old_points = np.array([[]])
        self.__lk_params = dict(winSize = (15, 15),
                 maxLevel = 4,
                 criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))
        self.__status = False
        self.on_tracker_resolve = EventHook()

    @property
    def status(self):
        return self.__status

    def start(self, frame, x, y):
        self.__old_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        self.__old_points = np.array([[x, y]], dtype=np.float32)
        self.__status = True
    
    def resolve(self, frame):
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        new_points, status, error = cv2.calcOpticalFlowPyrLK(
            self.__old_frame,
            gray_frame,
            self.__old_points,
            None,
            **self.__lk_params)
        self.__old_frame = gray_frame.copy()
        self.__old_points = new_points

        x, y = new_points.ravel()
        cv2.circle(frame, (x, y), 5, (0, 255, 0), -1)
        self.on_tracker_resolve.fire(self.__name, x, y)
