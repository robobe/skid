import logging
import traceback
import threading

log = logging.getLogger(__name__)

lock = threading.Lock()

class SingletonMeta(type):
    """
    The Singleton class can be implemented in different ways in Python. Some
    possible methods include: base class, decorator, metaclass. We will use the
    metaclass because it is best suited for this purpose.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """
        if cls not in cls._instances:
            #with lock:
            if cls not in cls._instances:
              instance = super().__call__(*args, **kwargs)
              cls._instances[cls] = instance
        return cls._instances[cls]


class EventHook(object):
  def __init__(self):
    self.__handlers = []

  def __iadd__(self, handler):
    self.__handlers.append(handler)
    return self

  def __isub__(self, handler):
    if handler in self.__handlers:
      self.__handlers.remove(handler)
    return self

  def fire(self, *args, **kwargs):
    for handler in self.__handlers:
      handler(*args, **kwargs)