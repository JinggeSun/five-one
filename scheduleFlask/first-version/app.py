import csv

from flask import Flask, jsonify
from flask_apscheduler import APScheduler
import mysql.connector
import os


class Config(object):  # 创建配置，用类PIP
    # 任务列表
    JOBS = [
        {  # 第1个任务，每隔5S执行一次
            'id': 'job2',
            'func': '__main__:method_test',  # 方法名
            'args': (1, 2),  # 入参
            'trigger': 'cron',  # interval表示循环任务，cron表示使用cron表达式
            'day_of_week': '*',
            'hour': '*',
            'minute': '*',
            'second': '*/55'
        }
    ]


app = Flask(__name__)
app.config.from_object(Config())  # 为实例化的flask引入配置


def method_test(obj1, obj2):
    print(obj1 + obj2)
    mysql_db = mysql.connector.connect(
        host="",
        user="root",
        passwd="",
        database=""
    )
    my_cursor = mysql_db.cursor()
    sql = "SELECT index_name,index_code FROM gs_index"
    my_cursor.execute(sql)
    my_result = my_cursor.fetchall()
    for x in my_result:
        print(x[0])
    my_cursor.close()
    mysql_db.close()
    path = '.././log/'
    if not os.path.exists(path):
        os.mkdir(path)
    f = open(path+'222.csv', 'w')
    writer = csv.writer(f)
    for i in my_result:
        writer.writerow(i)
    f.close()


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route("/table/list")
def table_list():
    mysql_db = mysql.connector.connect(
        host="",
        user="root",
        passwd="",
        database=""
    )
    my_cursor = mysql_db.cursor()
    sql = "SELECT index_name,index_code FROM gs_index"
    my_cursor.execute(sql)
    my_result = my_cursor.fetchall()
    return jsonify({"result": my_result})  # 返回布尔值


@app.route("/file/list")
def file_list():
    path = '../log/'
    filenames = os.walk(path)
    res_data = []
    for root, dirs, files in filenames:
        for file in files:
            res_data.append(os.path.join(root, file))
    return jsonify({"result": res_data})  # 返回布尔值


if __name__ == '__main__':
    scheduler = APScheduler()
    scheduler.init_app(app)
    scheduler.start()
    app.run()
