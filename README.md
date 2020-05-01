# five-one
五一学习记录
# Flask项目
定时从数据库中读取数据，追加或者新建到本地csv文件，然后有2个web api，1个是查看数据库数据列表，1个是查看csv文件
## 开发步骤
开发工具：pycharm
python版本：python3+
### 初版开发 First-Version
1. 新建flask项目，运行main方法，跑通hello world
#### 调度任务
1. pip3 install Flask-APScheduler
2. 编写job配置类，配置任务信息，使用corn表达式
3. 编写任务方法
4. app注册，main方法启动调度
5. python app.py 运行
#### 数据库链接
没有采用orm方式，使用jdbc方式
1. pip3 install mysql-connector
2. 连接数据库（ip，用户名，密码，数据库）
3. 获取cursor
4. 执行sql，execute，获取结果
5. 关闭游标，连接
#### csv文件操作
1. 使用自带的csv文件操作
2. os.walk获取文件，2个循环得到所有文件
3. jsonify展示