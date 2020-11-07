import logging
from utils.py_tools import SingletonMeta
import threading
import time
import os
import sys
sys.path.append(os.path.join(os.path.basename(__file__), ".."))
from fcu import context
from fcu.hw import video_stream
import cv2

log = logging.getLogger(__name__)


class tracker(metaclass=SingletonMeta):
    def __init__(self):
        self.__ctx = context.context()
        self.__camera = video_stream.VideoStream()
        self.__run()

    

    def start(self):
        log.info("Start tracker")
        t = threading.Thread(target=self.__run)
        t.setDaemon(True)
        t.setName("TrackerT")
        t.start()

    def __run(self):
        while True:
            ret, frame = self.__camera.read()
            if not ret:
                continue
            log.info(frame.shape)
            cv2.imshow("tracker", frame)
            self.__ctx.invoke_tracker_resolve(1, 1)
            cv2.waitKey(1)


