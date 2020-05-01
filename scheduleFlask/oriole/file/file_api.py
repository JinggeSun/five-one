from flask import Blueprint


file_hd = Blueprint('file', __name__)


@file_hd.route('/list')
def get_table_list():
    return 'file list'
