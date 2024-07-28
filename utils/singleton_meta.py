import threading

"""Define a singleton meta class derived from type"""
class SingletonMeta(type):
    """Dictionary to store singleton class instances"""
    _instances = {}

    """To ensure thread safe singleton implementation"""
    _lock = threading.Lock()

    """Override the call method to control how class is instantiated"""
    def __call__(cls, *args, **kwargs):
        """Acquire the lock for thread safety"""
        with cls._lock:
            """If class instance not exist in dictionary then create new instance"""
            if cls not in cls._instances:
                cls._instances[cls] = super().__call__()
        return cls._instances[cls]