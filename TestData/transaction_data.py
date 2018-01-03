# -*- coding=utf-8 -*-
import datetime
today = datetime.datetime.now().strftime("%Y-%m-%d")[:11]
today_1 = datetime.datetime.now().strftime("%Y%m%d")[:11]
yesterday = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime("%Y-%m-%d")[:11]


#插入交易数据

Upay_data="INSERT INTO `t_cp_order` VALUES ('1', '1514271807897', '1514273223906', 'DBDF', '%sDBDF', '%s6666', '', '2', '%s', '15:21:46', '00', '61288384777231321', '中国工商银行', '金地支行', 'ICBC', '赵华兵', '15111211030', 'RMB', '50000.00', '1', '8.00', null, null, null, null, null, null, null, null, null, '0', null, null, null, null, '0', '0', null, null, null, 'ICBC002', null, null, null, null, '0', '1', '%s 15:36:36', '%s 10:00:57');"%(today_1,today_1,today,today,today)
remote_Upay_data="INSERT INTO `t_cp_remote_order` VALUES ('1', '%s6666', null, 'Upay01', '中国工商银行', '61288384777231321', '金地支行', '61288384777231321', 'ICBC', '15111211030', '2', 'DBDF', '人民币', '5000.00', 'Upay01', null, '0', '%s', '10:26:40', '201712288888', '%s', null, null, '8.00', '0', '00', '%s 10:30:00', '%s 10:30:05');"%(today_1,yesterday,today,today,today)
HFpay_data_1="INSERT INTO `t_cp_order` VALUES ('2', '1514432615548', '', 'DBDF', '%sHFDBDF', '%s7777', '', '2', '%s', '15:21:46', '00', '61288384787645392', '中国工商银行', '高新支行', 'ICBC', '冯晨晨', '15111211030', 'RMB', '40000.00', '1', '8.00', null, null, null, null, null, null, null, null, null, '0', null, null, null, null, '0', '0', null, null, null, 'ICBC002', null, null, null, null, '0', '1', '%s 15:36:36', '%s 10:00:57');"%(today_1,today_1,today,today,today)
remote_HFpay_data_1="INSERT INTO `t_cp_remote_order` VALUES ('2', '%s7777', null, 'HFpay01', '中国工商银行', '61288384787645392', '高新支行', '61288384787645392', 'ICBC', '15111211030', '2', 'DBDF', '人民币', '4000.00', 'HFpay01', null, '0', '%s', '10:26:40', '201712287777', '%s', null, null, '8.00', '0', '00', '%s 10:30:00', '%s 10:30:05');"%(today_1,yesterday,today,today,today)

transaction_data=[Upay_data,remote_Upay_data,HFpay_data_1,remote_HFpay_data_1]
