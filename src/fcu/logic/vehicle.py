import logging
import os
import sys
import threading
import time
sys.path.append(os.path.join(os.path.basename(__file__), ".."))
from utils.py_tools import SingletonMeta
from fcu import context

log = logging.getLogger(__name__)


class vehicle(metaclass=SingletonMeta):
    def __init__(self):
        self.__ctx = context.context()
        self.__ctx.on_tracker_resolved += self.__tracker_handler

    def start(self):
        t = threading.Thread(target=self.__run)
        t.setDaemon(True)
        t.setName("VehicleT")
        t.start()

    def __run(self):
        while True:
            log.info("vehicle")
            time.sleep(1)

    def __tracker_handler(self, x, y):
        log.info(f"Tracker {x}, {y}")