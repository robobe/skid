import cv2
import sys
import numpy as np
from fcu.hw.gst import GstStream
import logging

log = logging.getLogger(__name__)

class VideoStream():
    def __init__(self):
        self.__source = GstStream()
        self.__source.start()

    def read(self):
        return self.__source.read()

    
