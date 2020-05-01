# five-one
五一学习记录
# Flask项目
定时从数据库中读取数据，追加或者新建到本地csv文件，然后有2个web api，1个是查看数据库数据列表，1个是查看csv文件
### 开发情况
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
### 更新版本 Oriole
新版本命名Oriole，对初版本各个组件进行封装
#### 数据库连接封装
1. 新建数据库工具类，所有数据库操作都封装在此
#### Flask-APScheduler学习
1. 集成到flask里面，动态添加任务（未完成）
2. 启动时，使用文件锁，保证只有1个进程启用调度