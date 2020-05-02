import atexit
import fcntl

from flask import Flask
from flask_apscheduler import APScheduler

scheduler = APScheduler()


def method_test(obj1, obj2):
    print("调度---> " + obj2 + obj1)


def scheduler_init(app):
    f = open("scheduler.lock", "wb")
    try:
        fcntl.flock(f, fcntl.LOCK_EX | fcntl.LOCK_NB)
        scheduler.init_app(app)
        scheduler.start()
    except Exception as e:
        print(e)

    def unlock():
        fcntl.flock(f, fcntl.LOCK_UN)
        f.close()
    atexit.register(unlock)


def create_app():
    app = Flask(__name__)
    # 启动定时任务
    scheduler_init(app)
    return app
