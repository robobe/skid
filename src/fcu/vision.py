import logging
from utils.py_tools import SingletonMeta
import threading
import time
from fcu import context

log = logging.getLogger(__name__)


class tracker(metaclass=SingletonMeta):
    def __init__(self, ctx):
        self.__ctx = ctx
        self.__run()
        
    def ctx(self):
        return self.__ctx

    def start(self):
        t = threading.Thread(target=self.__run)
        t.setDaemon(True)
        t.setName("TrackerT")
        t.start()

    def __run(self):
        while True:
            log.info("track")
            self.__ctx.invoke_tracker_resolve(1, 1)
            time.sleep(1)


