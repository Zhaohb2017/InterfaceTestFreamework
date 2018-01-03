# -*- coding=utf-8 -*-
import pymysql,os
try:
    from  sshtunnel import SSHTunnelForwarder
except ImportError:
    os.system("pip install sshtunnel")

def mysql_command(command):
    server = SSHTunnelForwarder(
        ('112.74.176.193', 22),  # 服务器地址
        ssh_username="novards",  # 登录服务器账号
        ssh_password="Novards2017",  # 登录服务器密码
        remote_bind_address=('rm-wz911y482te60z95ko.mysql.rds.aliyuncs.com', 3306)  # 服务器数据库地址，端口
    )

    server.start()


    # 本地访问地址必须为：127.0.0.1，端口为server.local_bind_port
    conn = pymysql.connections.Connection(host='127.0.0.1', user='nova', port=server.local_bind_port,
                                          password='Nova2017', charset='utf8mb4', database='cpcr-boss')
    cur = conn.cursor(cursor=pymysql.cursors.DictCursor)  # 游标设置为字典类型
    try:
        cur.execute(command)
        # fetchall:是获取所有的数据，fetchmany(3)是获取前3行数据,fetchone是获取第一行数据
        results = cur.fetchall()
        conn.commit()
    except:
        conn.rollback()
    conn.close()
    server.stop()
    # return results




