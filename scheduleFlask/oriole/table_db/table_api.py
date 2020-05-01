from flask import Blueprint, jsonify

from oriole.db.DbUtil import DbUtil

table_hd = Blueprint('table', __name__)


@table_hd.route('/list')
def get_table_list():
    db1 = DbUtil()
    db1.connect()
    # 查找某一行
    print(db1.count('gs_index', None, None))
    vas = db1.findAll("select * from gs_index")
    db1.close()
    return jsonify({"result": vas})  # 返回布尔值
