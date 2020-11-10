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
from fcu.settings import Settings

log = logging.getLogger(__name__)

class vehicle(metaclass=SingletonMeta):
    def __init__(self):
        log.info("Vehicle start")
        self.__ctx = context.context()
        self.settings = Settings()
        self.__ctx.on_tracker_resolved += self.__tracker_handler
        self.__mavlink = MavNode()
        
        self.__steering_pid = None
        self.__throttle_pid = None
        self.__x_lpf = lpf(factor = 0)
        self.__y_lpf = lpf(factor = 0)
        self.__init_pid()
        self.__pid_norm_pwm = map_utils(-1, 1, 2000, 1000)
        self.__pid_norm_throttle = map_utils(-1, 1, 1100, 1950)
        log.info("Vehicle start1")

    def __init_pid(self):
        self.__throttle_pid = PID(
            P=self.settings["throttle_pid_p"],
            I=self.settings["throttle_pid_i"],
            D=self.settings["throttle_pid_d"])
        
        self.__throttle_pid.setOutMinLimit(-1)
        self.__throttle_pid.setOutMaxLimit(1)

        self.__throttle_pid.SetPoint = 0

        p = self.settings.get("steering_pid_p")
        self.__steering_pid = PID(P=p,
             I=self.settings["steering_pid_i"],
             D=self.settings["steering_pid_d"])
        
        log.info(f"PID p:{p}")
        self.__steering_pid.setOutMinLimit(-1)
        self.__steering_pid.setOutMaxLimit(1)
        self.__steering_pid.SetPoint = 0

    def start(self):
        t = threading.Thread(target=self.__run)
        t.setDaemon(True)
        t.setName("VehicleT")
        t.start()
        

    def __run(self):
        log.info("Vehicle handler start")
        self.__mavlink.connect()
        while True:
            # log.info("vehicle")
            time.sleep(1)

    def __tracker_handler(self, x, y):
        x = self.__x_lpf.update(x)
        y = self.__y_lpf.update(y)

        self.__steering_pid.update(x)
        self.__throttle_pid.update(y)

        sterring_pwm = int(self.__pid_norm_pwm.map_range(self.__steering_pid.output))
        throttle_pwm = int(self.__pid_norm_throttle.map_range(self.__throttle_pid.output))
        log.info(f"Tracker {x},{y}, throttle: {throttle_pwm}, sterring: {sterring_pwm} ")
        self.__mavlink.sticks_controls(sterring_pwm, throttle_pwm)