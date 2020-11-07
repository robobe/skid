import logging
import os
import sys
import threading
import time
sys.path.append(os.path.join(os.path.basename(__file__), ".."))
from utils.py_tools import SingletonMeta
from utils.rc_tools import lpf, map_utils
from fcu import context
from fcu.hw.mav import MavNode
from utils.pid import PID

log = logging.getLogger(__name__)

class vehicle(metaclass=SingletonMeta):
    def __init__(self):
        self.__ctx = context.context()
        self.__ctx.on_tracker_resolved += self.__tracker_handler
        self.__mavlink = MavNode()
        self.__steering_pid = None
        self.__x_lpf = lpf()
        self.__init_pid()
        self.__pid_norm_pwm = map_utils(-1, 1, 1000, 2000)

    def __init_pid(self):
        self.__steering_pid = PID()
        self.__steering_pid.SetPoint = 0

    def start(self):
        t = threading.Thread(target=self.__run)
        t.setDaemon(True)
        t.setName("VehicleT")
        t.start()
        

    def __run(self):
        log.info("Vehicle handler start")
        # self.__mavlink.connect()
        while True:
            # log.info("vehicle")
            time.sleep(1)

    def __tracker_handler(self, x, y):
        x = self.__x_lpf.update(x)
        self.__steering_pid.update(x)
        pwm =  round(self.__pid_norm_pwm.map_range(self.__steering_pid.output), 0)
        log.info(f"Tracker {x}, {pwm}")