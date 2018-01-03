# -*- coding=utf-8 -*-
from CpcrBoss import main
from TestData.mysql_data import *
from TestData.connect_mysql import mysql_command
from TestData.transaction_data import *

if __name__ == "__main__":
    #初始化数据
    for sql in clear_data:
        mysql_command(sql)
    #添加数据
    for data in insert_data:
        mysql_command(data)
    #添加交易数据
    for trc_data in transaction_data:
        mysql_command(trc_data)
    print 'Done!'
    # main('TestCase/cpcrBoss_TestCase.xlsx')
