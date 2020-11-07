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
from utils.rc_tools import map_utils

log = logging.getLogger(__name__)

class fuse(metaclass=SingletonMeta):
    def __init__(self):
        self.__ctx = context.context()
        self.__camera = None
        self.__frame = None
        self.__trackers = [lk()]
        self.__results = {}
        self.__camera_norm_horizontal  = map_utils(0, 640, -1, 1)
        self.__camera_norm_vertical  = map_utils(0, 480, -1, 1)

        viewer.on_point_selected += self.__point_selected_handler
        for t in self.__trackers:
            t.on_tracker_resolve += self.__tracker_resolve_handler
    
    #region cb
    def __tracker_resolve_handler(self, name, x, y):
        # self.__ctx.invoke_tracker_resolve(x, y)
        self.__results[name] = (x,y)
        self.__trackers_fuse()
    
    def __point_selected_handler(self, x, y):
        for t in self.__trackers:
            t.start(self.__frame, x, y)
        log.warn(x)

    #endregion cb

    def start(self):
        log.info("Start fuse")
        t = threading.Thread(target=self.__run)
        t.setDaemon(True)
        t.setName("fuse")
        t.start()

    #region private
    def __trackers_fuse(self):
        for name, result in self.__results.items():
            x, y = result
            norm_x = round(self.__camera_norm_horizontal.map_range(x), 3)
            norm_y = round(self.__camera_norm_vertical.map_range(y), 3)
            self.__ctx.invoke_tracker_resolve(norm_x, norm_y)

    def __run(self):
        self.__camera = video_stream.VideoStream()
        while True:
            ret, self.__frame = self.__camera.read()
            if not ret:
                continue
            
            for t in self.__trackers:
                if t.status:
                    t.resolve(self.__frame)

            viewer.show(self.__frame)
            
    #endregion private

