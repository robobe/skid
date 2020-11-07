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
import numpy as np
from fcu.logic.lk_tracker import lk
import fcu.logic.video_viewer as viewer

log = logging.getLogger(__name__)

class fuse(metaclass=SingletonMeta):
    def __init__(self):
        self.__ctx = context.context()
        self.__camera = video_stream.VideoStream()
        self.__frame = None
        self.__tracker = lk()
        viewer.on_point_selected += self.__point_selected_handler
        self.__tracker.on_tracker_resolve += self.__tracker_resolve_handler
        self.__run()
        
    #region cb
    def __tracker_resolve_handler(self, x, y):
        self.__ctx.invoke_tracker_resolve(x, y)
    
    def __point_selected_handler(self, x, y):
        self.__tracker.start(self.__frame, x, y)
        log.warn(x)

    #endregion cb

    def start(self):
        log.info("Start fuse")
        t = threading.Thread(target=self.__run)
        t.setDaemon(True)
        t.setName("fuse")
        t.start()

    def __run(self):
        while True:
            ret, self.__frame = self.__camera.read()
            if not ret:
                continue
            
            if self.__tracker.status:
                self.__tracker.resolve(self.__frame)

            viewer.show(self.__frame)
            


