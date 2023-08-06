import threading


def singleton(cls):
    instance = {}
    lock = threading.Lock()

    def wrap(*args, **kwargs):
        with lock:
            if cls not in instance:
                instance[cls] = cls(*args, **kwargs)
        return instance[cls]
    return wrap
