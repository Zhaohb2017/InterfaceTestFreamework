# -*- coding=utf-8 -*-
import datetime,time,random
"""
清除数据:
1.支付公司管理表 2支付通道管理表 3支付通道银行管理表 4通道配置表
1.一、二级商户管理表 2一级商户费率管理表 3.商户限额管理表

"""
today = datetime.datetime.now().strftime("%Y-%m-%d")[:11]
tomorrow =(datetime.datetime.now() + datetime.timedelta(days=30)).strftime("%Y-%m-%d")[:11]
random_1 = random.randrange(1,5)
random_2 = random.randrange(6,10)

clear_data =['TRUNCATE TABLE t_cp_pay_company;','TRUNCATE TABLE t_cp_pay_channel;','TRUNCATE TABLE t_cp_bank;',"TRUNCATE TABLE t_cp_bank_pay_channel;",
             "TRUNCATE TABLE t_cp_mer_base_info;","TRUNCATE TABLE t_cp_fee;","TRUNCATE TABLE t_cp_mer_quota;",
             ]

#创建第三方支付管理数据
company_ZHB="INSERT INTO `t_cp_pay_company` VALUES ('3', 'ZHB001', 'ZHB测试支付公司', '0', '%s 14:28:39', '1', '%s 14:28:38', null);"%(today,today)
channel_ZHB="INSERT INTO `t_cp_pay_channel` VALUES ('11', 'ZHB001', 'ZHB测试支付通道', 'ZHB001', '1', '10', '9.00000', '1', '15:20:20', '15:20:20', '0', '0', '1', '%s 14:39:22', '1', '%s 14:39:21', null);"%(today,today)
channel_SZ="INSERT INTO `t_cp_pay_channel` VALUES ('12', 'SZ0001', '深圳测试支付通道', 'ZHB001', '2', '10', '0.10000', '1', '18:01:11', '18:01:11', '1', '0', '1', '%s 17:01:59', '1', '%s 17:01:59', null);"%(today,today)
channel_FT="INSERT INTO `t_cp_pay_channel` VALUES ('13', 'FT0003', '福田测试支付通道', 'ZHB001', '3', '10', '0.10000', '2', '18:01:11', '18:01:11', '1', '1', '0', '%s 17:02:43', '1', '%s 17:02:43', null);"%(today,today)
bank_ZHB="INSERT INTO `t_cp_bank` VALUES ('2', 'ZHB123', 'ZHB123', 'ZHB测试银行', 'ZHB测试银行', '1', null, '1', '%s 14:42:18', null);"%today
# 支付通道配置
ban_ZHB_channel="INSERT INTO `t_cp_bank_pay_channel` VALUES ('2', 'ZHB123', 'ZHB001', '0.00', '100.00', '1000.00', '1', null, '1', '%s 14:42:18', null);"%today
#新增一级商户
one_mch="INSERT INTO `t_cp_mer_base_info` VALUES (%d, '1514271807897', 'ZHB测试商户', '赵华兵测试公司', null, 'TEST000000001', '周小博', '1', '443030199903292303', null, null, '13600000000', null, null, '虚拟地址2047号', '虚拟业务', 'https://www.fake.com', null, null, '这是测试', null, '1', null, '0', null, null, null, null, null, '1', '%s 15:03:27', null);"%(random_1,today)
#新增二级商户
tow_mch="INSERT INTO `t_cp_mer_base_info` VALUES (%d, '1514273223906', 'ZHB二级商户', null, null, null, null, null, null, '广东省', '周小博', '13600000000', null, null, null, null, null, null, null, null, null, '0', '1514271807897', '3', '0', '1', '1', null, '%s 15:27:04', '1', '%s 15:27:03', null);"%(random_2,today,today)
#一级商户费率
one_mch_fee="INSERT INTO `t_cp_fee` VALUES (%d, 'ZHB123', 'all', '1514271807897', '00', '%s', '%s', '0', null, null, '%s 15:32:43', null);"%(random_1,today,tomorrow,today)
#新增一级商户限额管理数据
mch_quota="INSERT INTO `t_cp_mer_quota` VALUES (%d, '1514271807897', 'all', '100.00', '1000.00', '10000.00', '1', '%s 15:42:07', null, '%s 15:42:06', null);"%(random_1,today,today)
#新增节假日
holiday="INSERT INTO `t_cp_holiday` VALUES ('1', '2017', '2017-01-04', '2017-12-29', '10000011000001100000110000011000001100000110000011000001100000110000011000001100000110000011000001100000110000011000001100000110000011000001100000110000011000001100000110000011000001100000110000011000001100000110000011000001100000110000011000001100000110000011000001100000110000011000001100000110000011000001100000100000011000001100000110000011000001100000110000011', '1', '2017-12-26 19:18:47', '1', '2017-12-26 19:18:47', null);"
insert_data=[company_ZHB,channel_ZHB,channel_SZ,channel_FT,bank_ZHB,one_mch,tow_mch,one_mch_fee,mch_quota,ban_ZHB_channel,holiday]



