# -*- coding=utf-8 -*-
import datetime,time,random
"""
清除数据:
1.支付公司管理表 2支付通道管理表 3支付通道银行管理表 4通道配置表
1.一、二级商户管理表 2一级商户费率管理表 3.商户限额管理表

"""
today = datetime.datetime.now().strftime("%Y-%m-%d")[:11]
tomorrow =(datetime.datetime.now() + datetime.timedelta(days=30)).strftime("%Y-%m-%d")[:11]
random_1 = random.randrange(1,10)
random_2 = random.randrange(11,20)

clear_data =['TRUNCATE TABLE t_cp_pay_company;','TRUNCATE TABLE t_cp_pay_channel;','TRUNCATE TABLE t_cp_bank;',"TRUNCATE TABLE t_cp_bank_pay_channel;",
             "TRUNCATE TABLE t_cp_mer_base_info;","TRUNCATE TABLE t_cp_fee;","TRUNCATE TABLE t_cp_mer_quota;",
             ]

#创建第三方支付管理数据
company_Ali="INSERT INTO `t_cp_pay_company` VALUES ('3', 'Alipay02', '阿里支付公司', '1', '%s 14:28:39', '0', '%s 14:28:38', null);"%(today,today)
company_WX="INSERT INTO `t_cp_pay_company` VALUES ('4', 'WXPay02', '微信支付公司', '1', '%s 14:28:39', '0', '%s 14:28:38', null);"%(today,today)
company_U="INSERT INTO `t_cp_pay_company` VALUES ('5', 'Upay02', '银联支付公司', '1', '%s 14:28:39', '0', '%s 14:28:38', null);"%(today,today)
company_hf="INSERT INTO `t_cp_pay_company` VALUES ('6', 'HFpay02', '恒丰银行支付公司', '1', '%s 14:28:39', '0', '%s 14:28:38', null);"%(today,today)
channel_Ali="INSERT INTO `t_cp_pay_channel` VALUES ('11', 'Alipay01', '阿里单笔代付', 'Alipay02', '1', '10', '9.00000', '1', '15:20:20', '15:20:20', '0', '0', '1', '%s 14:39:22', '1', '%s 14:39:21', null);"%(today,today)
channel_WX="INSERT INTO `t_cp_pay_channel` VALUES ('12', 'WXPay01', '微信单笔代付', 'WXPay02', '3', '10', '0.10000', '1', '18:01:11', '18:01:11', '1', '0', '1', '%s 17:01:59', '1', '%s 17:01:59', null);"%(today,today)
channel_U="INSERT INTO `t_cp_pay_channel` VALUES ('13', 'Upay01', '银联单笔代付', 'Upay02', '2', '10', '0.10000', '2', '18:01:11', '18:01:11', '1', '1', '1', '%s 17:02:43', '1', '%s 17:02:43', null);"%(today,today)
channel_hf="INSERT INTO `t_cp_pay_channel` VALUES ('14', 'HFpay01', '恒丰单笔代付', 'HFpay02', '2', '10', '0.10000', '1', '10:31:17', '10:31:19', '1', '0', '1', '%s 10:41:41', '1', '%s 10:41:41', null);"%(today,today)
bank_ICBC="INSERT INTO `t_cp_bank` VALUES ('2', 'ICBC002', 'ICBC002', '中国工商银行', '中国工商银行', '1', null, '1', '%s 14:42:18', null);"%today
bank_CBC="INSERT INTO `t_cp_bank` VALUES ('3', 'CBC939', 'CBC939', '建设银行', 'CBC', '1', null, '1', '%s 13:56:18', null);"%today
# 支付通道配置
ban_ICBC_channel="INSERT INTO `t_cp_bank_pay_channel` VALUES ('2', 'ICBC002', 'Alipay01', '0.00', '100.00', '1000.00', '1', null, '1', '%s 14:42:18', null);"%today
bank_CBC_channel="INSERT INTO `t_cp_bank_pay_channel` VALUES ('3', 'CBC939', 'HFpay01', '2.00', '10000.00', '10000000.00', '1', null, '1', '%s 13:56:18', null);"%today
ban_ICBC_channel_Upay="INSERT INTO `t_cp_bank_pay_channel` VALUES ('5', 'ICBC002', 'Upay01', '0.00', '10000.00', '100000.00', '1', null, '1', '%s 14:02:04', null);"%today
#新增一级商户
one_mch_lq="INSERT INTO `t_cp_mer_base_info` VALUES ('5', '1514432615548', '深圳路桥设计有限公司', '深圳路桥设计有限公司', null, 'SZ201702', '周小博', '1', '443030199903292303', null, null, '13600000000', null, null, '虚拟地址2047号', '实体业务', 'https://www.fake.com', null, null, '专注桥梁设计，房屋设计公司', null, '1', null, '0', null, null, null, null, '%s 17:15:17', '1', '%s 11:43:35', '1');"%(today,today)
one_mch_szt="INSERT INTO `t_cp_mer_base_info` VALUES (1, '1514271807897', '深圳通科技有限公司', '阿里支付公司', null, 'TEST000000001', '周小博', '1', '443030199903292303', null, null, '13600000000', null, null, '虚拟地址2047号', '虚拟业务', 'https://www.fake.com', null, null, '深圳通公司', null, '1', null, '0', null, null, null, null, '%s 17:15:17', '1', '%s 15:03:27', '1');"%(today,today)
one_mch_js="INSERT INTO `t_cp_mer_base_info` VALUES (2, '1514370951855', '锦尚科技', '锦尚科技有限公司', null, 'JS00002', '周小博', '1', '443030199903292303', null, null, '13600000000', null, null, '虚拟地址2047号', '虚拟业务', 'https://www.fake.com', null, null, '锦尚科技', null, '0', null, '0', null, null, null, null, '%s 17:15:17', '1', '%s 18:35:51', '1');"%(today,today)
#新增二级商户
tow_mch="INSERT INTO `t_cp_mer_base_info` VALUES (3, '1514273223906', '百事通有限公司', null, null, null, null, null, null, '广东省', '周小博', '13600000000', null, null, null, null, null, null, null, null, null, '1', '1514271807897', '3', '0', '1', '1', null, '%s 15:27:04', '1', '%s 15:27:03', '1');"%(today,today)
HC="INSERT INTO `t_cp_mer_base_info` VALUES ('4', '1514371034235', '皇城老妈餐饮公司', null, null, null, null, null, null, '广东省', '周小博', '13600000000', null, null, null, null, null, null, null, null, null, '0', '1514370951855', '18', '0', '0', '1', null, '%s 18:37:14', '1', '%s 18:47:47', '1');"%(today,today)
#一级商户费率
szt_fee="INSERT INTO `t_cp_fee` VALUES (2, 'ICBC002', 'all', '1514271807897', '00', '%s', '%s', '1', null, null, '%s 15:32:43', null);"%(today,tomorrow,today)
lp_fee="INSERT INTO `t_cp_fee` VALUES ('3', 'all', 'all', '1514432615548', 'all', '%s', '%s', '1', null, null, '%s 14:07:26', null);"%(today,tomorrow,today)
#新增一级商户限额管理数据
lq_quota="INSERT INTO `t_cp_mer_quota` VALUES ('2', '1514432615548', 'DBDF', '1.00', '100000.00', '1000000.00', '1', '%s 11:53:25', null, '%s 11:53:25', null);"%(today,today)
mch_quota="INSERT INTO `t_cp_mer_quota` VALUES ('1', '1514271807897', 'all', '100.00', '1000.00', '10000.00', '1', '%s 15:42:07', null, '%s 15:42:06', null);"%(today,today)
js_quota="INSERT INTO `t_cp_mer_quota` VALUES ('3', '1514370951855', 'BTDF', '100.00', '1000.00', '10000.00', '1', '%s 14:21:55', null, '%s 14:21:55', null);"%(today,today)
#新增节假日
holiday="INSERT INTO `t_cp_holiday` VALUES ('1', '2017', '2017-01-04', '2017-12-29', '10000011000001100000110000011000001100000110000011000001100000110000011000001100000110000011000001100000110000011000001100000110000011000001100000110000011000001100000110000011000001100000110000011000001100000110000011000001100000110000011000001100000110000011000001100000110000011000001100000110000011000001100000100000011000001100000110000011000001100000110000011', '1', '2017-12-26 19:18:47', '1', '2017-12-26 19:18:47', null);"
insert_data=[company_Ali,company_WX,company_U,channel_hf,channel_Ali,channel_WX,company_hf,channel_U,bank_ICBC,bank_CBC,one_mch_szt,one_mch_js,one_mch_lq,tow_mch,HC,szt_fee,lp_fee,mch_quota,ban_ICBC_channel,holiday,lq_quota,js_quota,ban_ICBC_channel_Upay]



