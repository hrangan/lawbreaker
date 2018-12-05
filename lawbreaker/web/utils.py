from time import time, sleep
import threading

from datetime import datetime, timedelta


def spawn_daemon(func, interval):
    def _daemon():
        last_run = datetime.now()
        while True:
            if datetime.now() - last_run > timedelta(seconds=interval):
                func()
                last_run = datetime.now()
            sleep(interval/20)

    thread = threading.Thread(target=_daemon)
    thread.daemon = True
    thread.start()


def timing(func):
    def _wrapper(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        end = time()
        print('%s: %s' % (func.__name__, str(end-start)))
        return result
    return _wrapper
