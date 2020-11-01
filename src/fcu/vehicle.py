import logging
from utils.py_tools import SingletonMeta
import threading
import time
from fcu import context

log = logging.getLogger(__name__)


class vehicle(metaclass=SingletonMeta):
    def __init__(self):
        ctx = context.context()
        print(id(ctx))
        ctx.on_tracker_resolved += self.__tracker_handler

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