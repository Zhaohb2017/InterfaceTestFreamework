# -*- coding=utf-8 -*-
from CpcrBoss import main
from connect_mysql import mysql_command
from mysql_data import *

if __name__ == "__main__":
    #初始化数据
    for sql in clear_data:
        mysql_command(sql)
    #添加数据
    for data in insert_data:
        mysql_command(data)
    print 'Done!'
    main('TestCase/cpcrBoss_TestCase.xlsx')
