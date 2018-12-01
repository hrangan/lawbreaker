import time
import threading

from datetime import datetime, timedelta


def spawn_daemon(func, interval):
    def _daemon():
        last_run = datetime.now()
        while True:
            if datetime.now() - last_run > timedelta(seconds=interval):
                func()
                last_run = datetime.now()
            time.sleep(interval/20)

    thread = threading.Thread(target=_daemon)
    thread.daemon = True
    thread.start()
