import logging
import json
import logging.config
import os
from fcu import vision

def run():
    log.info("Run")
    vision.start()

def __init_logging():
    config_file = os.path.join(os.path.dirname(__file__), "log.config")
    with open(config_file, "r") as fd:
        config = json.load(fd)

    logging.config.dictConfig(config["logging"])

if __name__ == "__main__":
    __init_logging()
    log = logging.getLogger(__name__)
    log.info('start')
    run()