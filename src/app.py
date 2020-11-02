import logging
import json
import logging.config
import os
import sys
from fcu import vision, context, vehicle as Vehicle
import signal


def run():
    ctx = context.context()
    ctx.on_tracker_resolved += cb
    ctx.invoke_tracker_resolve(1,2)
    
    exit()
    vehicle = Vehicle.vehicle(ctx)
    tracker = vision.tracker(ctx)
    exit()
    tracker.start()
    vehicle.start()

def cb(x,y):
    print(x)

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
    run()
    print('Press Ctrl+C')
    signal.pause()
