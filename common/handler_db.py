import pymysql

from common.handler_conf import Config


class HandleDB:
    def __init__(self, host, port, database, user, password, charset):
        self._con = pymysql.connect(host=host,
                                    port=port,
                                    database=database,
                                    user=user,
                                    password=password,
                                    charset=charset)
        self._cursor = self._con.cursor()

    def fetchall(self, sql):
        self._cursor.execute(sql)
        return self._cursor.fetchall()

    def fetchone(self):
        self._cursor.execute(sql)
        return self._cursor.fetchone()

    def insert(self, sql, data):
        self._cursor.execute(sql, data)
        self._cursor.commit()
        return self._cursor.lastrowid

    def update(self, sql, data):
        self._cursor.execute(sql, data)
        self._cursor.commit()
        return self._cursor.rowcount

    def delete(self, sql, data):
        self._cursor.execute(sql, data)
        self._cursor.commit()
        return self._cursor.rowcount

    def close(self):
        self._cursor.close()
        self._con.close()


if __name__ == '__main__':
    conf = Config
    cp = Config('../conf/env.ini')

    host = cp.get('db', 'host')
    port = cp.getint('db', 'port')
    database = cp.get('db', 'database')
    user = cp.get('db', 'user')
    password = cp.get('db', 'password')
    charset = cp.get('db', 'charset')

    sql = "select * from Persons"
    db = HandleDB(host, port, database, user, password, charset)
    print(db.fetchall(sql))
    db.close()
