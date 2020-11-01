import logging
from utils.py_tools import SingletonMeta
import threading
import time
from utils.py_tools import EventHook

log = logging.getLogger(__name__)


class context(metaclass=SingletonMeta):
    def __init__(self):
        self.on_tracker_resolved = EventHook()
        print(f"------------{self.on_tracker_resolved}-------------")

    def invoke_tracker_resolve(self, x, y):
        print(f"------------{self.on_tracker_resolved}-------------")
        self.on_tracker_resolved.fire(x, y)
