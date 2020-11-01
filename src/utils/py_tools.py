import logging
import traceback

log = logging.getLogger(__name__)

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
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class EventHook(object):
  def __init__(self):
    self.__handlers = []

  def __iadd__(self, handler):
    self.__handlers.append(handler)

  def __isub__(self, handler):
    self.__handlers.remove(handler)

  def fire(self, *args, **kwargs):
    for handler in self.__handlers:
        try:
            handler(*args, **kwargs)
        except:
            log.error("Event invoke failed")
            log.error(traceback.print_exc())

  def clearObjectHandlers(self, inObject):
    for theHandler in self.__handlers:
      if theHandler.im_self == inObject:
          self.__handlers.remove(theHandler)