import sqlite3
def insert_sql(sql_name, table_name, time, all_index, pc_index, wise_index):
    conn = sqlite3.connect(sql_name + '.sqlite3')
    curs = conn.cursor()
    try:
        curs.execute('CREATE TABLE %s(日期 varchar (30),总搜索指数 int (20000),PC端指数 int(20000), 移动端指数 int(20000))' % (table_name))
    except:
        pass

    exc = "insert into %s values('%s', '%d', '%d','%d')" %(table_name,time, all_index, pc_index, wise_index)
    curs.execute(exc)
    conn.commit()

def insert_sql2(sql_name, table_name, time, index):
    conn = sqlite3.connect(sql_name + '.sqlite3')
    curs = conn.cursor()
    try:
        curs.execute('CREATE TABLE %s(日期 varchar (30),总资讯指数 int (20000))' % (table_name))
    except:
        pass

    exc = "insert into %s values('%s', '%d')" %(table_name,time, index)
    curs.execute(exc)
    conn.commit()