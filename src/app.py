import logging
import json
import logging.config
import os
import sys
from fcu import context
from fcu.logic import fuse, vehicle as Vehicle
import signal


def run():
    ctx = context.context()
    vehicle = Vehicle.vehicle()
    sensors = fuse.fuse()
    
    sensors.start()
    vehicle.start()

def __init_logging():
    config_file = os.path.join(os.path.dirname(__file__), "log.config")
    with open(config_file, "r") as fd:
        config = json.load(fd)

    logging.config.dictConfig(config["logging"])

def signal_handler(sig, frame):
    print('You pressed Ctrl+C!')
    sys.exit(0)

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    __init_logging()
    log = logging.getLogger(__name__)
    log.info('start')
    # run()
    from fcu.settings import Settings
    s = Settings()
    print(s["steering_pid_p"])
    print('Press Ctrl+C')
    signal.pause()
