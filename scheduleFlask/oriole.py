# Oriole入口文件


from flask import Flask

from oriole.file.file_api import file_hd
from oriole.scheduler.factory import create_app
from oriole.table_db.table_api import table_hd
from oriole.scheduler.scheduler_api import scheduler_hd

app = Flask(__name__)
app = create_app()
app.register_blueprint(table_hd, url_prefix='/table')
app.register_blueprint(file_hd, url_prefix='/file')
app.register_blueprint(scheduler_hd, url_prefix='/sch')


if __name__ == '__main__':
    app.run()

