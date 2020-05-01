
from flask import Blueprint, jsonify, json

from oriole.scheduler.factory import scheduler

scheduler_hd = Blueprint('scheduler', __name__)


@scheduler_hd.route('/list')
def get_scheduler_list():
    scheduler.add_job(func=hello,id='test_3one', trigger='interval',seconds=10)
    return "ssss"


@scheduler_hd.route('/jobs')
def get_scheduler_jobs():
    data = scheduler.get_jobs()
    print(data[0])
    print(type(data))
    return jsonify({'ss':data[0]})
    #return json.dumps(str1, ensure_ascii=False)


def hello():
    print("ddddd")
