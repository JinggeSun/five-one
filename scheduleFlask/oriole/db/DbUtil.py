import mysql.connector


def init_connect():
    db = DbUtil(host='47.104.2.74', username='root', password='/H#aPd%yf99lwypt', database='gsipDMP')
    db.connect()
    return db


class DbUtil:
    sql = []
    conn = None
    db = None

    # 构造函数
    def __init__(self, host='47.104.2.74', username='root', password='/H#aPd%yf99lwypt', database='gsipDMP', port=3306, charset='utf8',
                 tablePrefix='', raise_on_warnings=True):
        self.host = host
        self.username = username
        self.password = password
        self.database = database
        self.port = int(port)
        self.charset = charset
        self.tablePrefix = tablePrefix
        self.raise_on_warnings = raise_on_warnings

    def connect(self, force=False):
        if self.conn is None or force is True:
            try:
                self.conn = mysql.connector.connect(host=self.host, user=self.username,
                                                    password=self.password, database=self.database, port=self.port,
                                                    raise_on_warnings=self.raise_on_warnings)
                self.db = self.conn.cursor(dictionary=True, buffered=True)
                if self.charset is not None:
                    self.query(
                        "SET character_set_connection='%s', character_set_results='%s', character_set_client=binary"
                        % (self.charset, self.charset))
            except Exception as err:
                raise Exception(err)
        return self.conn

    def count(self, table='', where=None, sql=None):
        count = 0
        if not sql:
            where = where if where else '1=1'
            sql = "SELECT COUNT(1) AS NUM FROM %s WHERE %s" % (
                self.table(table), where)
        self.query(sql)
        rs = {}
        rs = self.db.fetchone()
        if rs is not None:
            count = list(rs.values())[0]
        return count

    def table(self, tableName):
        return '%s%s' % (self.tablePrefix, tableName)

    def query(self, sql, params=None):
        self.sql.append(sql)
        if params:
            t = type(params)
            if t == dict:
                return self.db.execute(sql, params)
            elif t == list:
                return self.db.executemany(sql, params)
        return self.db.execute(sql, params)

    def findAll(self, sql=None):
        self.query(sql)
        return self.db.fetchall()

    def close(self):
        self.db.close()


if __name__ == '__main__':
    db1 = DbUtil(host='', username='root', password='', database='gsipDMP')
    db1.connect()
    # 查找某一行
    print(db1.count('gs_index', None, None))
    vas = db1.findAll("select * from gs_index")
    print(vas)
