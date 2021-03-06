import sys

sys.path.append('../')
import sqlparse
import pymysql
from applications.config.database import HOST, USERNAME, PASSWORD, DATABASE, PORT


def is_exist_database():
    db = pymysql.connect(
        host=HOST,
        port=int(PORT),
        user=USERNAME,
        password=PASSWORD,
        charset='utf8mb4')
    cursor1 = db.cursor()
    sql = f"select * from information_schema.SCHEMATA" \
          f" WHERE SCHEMA_NAME = '{DATABASE}';"
    res = cursor1.execute(sql)
    db.close()
    return res


def init_database():
    db = pymysql.connect(
        host=HOST,
        port=int(PORT),
        user=USERNAME,
        password=PASSWORD,
        charset='utf8mb4')
    cursor1 = db.cursor()
    sql = "CREATE DATABASE IF NOT EXISTS %s" % DATABASE
    res = cursor1.execute(sql)
    db.close()
    return res


def execute_fromfile(filename):
    db = pymysql.connect(
        host=HOST,
        port=int(PORT),
        user=USERNAME,
        password=PASSWORD,
        database=DATABASE,
        charset='utf8mb4')
    fd = open(filename, 'r', encoding='utf-8')
    cursor = db.cursor()
    sqlfile = fd.read()
    sqlfile = sqlparse.format(sqlfile, strip_comments=True).strip()

    sqlcommamds = sqlfile.split(';')

    for command in sqlcommamds:
        try:
            cursor.execute(command)
            db.commit()

        except Exception as msg:

            db.rollback()
    db.close()


def init_db():
    if is_exist_database():
        print(f'Database {DATABASE} is existed')
        return
    if init_database():
        print('Database %s create succ' % str(DATABASE))
    execute_fromfile('pear.sql')
    print('Table create succ')
    print('Database config done')


if __name__ == '__main__':
    init_db()

