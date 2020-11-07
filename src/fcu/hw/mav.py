from threading import Thread
import traceback
import time
from dronekit import connect, VehicleMode, LocationGlobal, LocationGlobalRelative
import logging

log = logging.getLogger(__name__)

class MavNode():
    def __init__(self, cs = "udp:127.0.0.1:14560"):
        # super(MavNode,self).__init__(name="mavlink", daemon=True, target=self.run)
        self.__vehicle = None
        self.__cs = cs

    # def run(self):
    #     self.connect()

    def connect(self):
        self.__vehicle = connect(self.__cs, wait_ready=True)
        while not self.__vehicle.is_armable:
            log.warn("waiting for vehicle initialise")
            time.sleep(1)

        self.__vehicle.mode = VehicleMode("MANUAL")
        self.__vehicle.armed = True

        while not self.__vehicle.armed:
            log.info("Waiting for arming...")
            time.sleep(1)
        log.info("Vehicle ready..")