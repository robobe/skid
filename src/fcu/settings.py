import os
import sys
import logging
sys.path.append(os.path.join(os.path.basename(__file__), ".."))
from utils.py_tools import SingletonMeta
from fcu import context
import json

log = logging.getLogger(__name__)

CONFIG_FILE = "settings.json"

class Settings(metaclass=SingletonMeta):
    def __init__(self):
        self.__ctx = context.context()
        self.__data = None
        self.__load()

    def __load(self):
        dir_name = os.path.dirname(__file__)
        s_file = os.path.join(dir_name, CONFIG_FILE)
        with (open(s_file, "r")) as f:
            self.__data = json.load(f)

    def get(self, name):
        return self.__data[name]

    def __getitem__(self, key):
        return self.__data[key]



