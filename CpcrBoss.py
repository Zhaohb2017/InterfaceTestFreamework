#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Todo：接口自动化测试
# Author：赵华兵
# Data : 2017-12-7
import json,requests
import time
import re
import logging
import os,sys
'''
sys.setdefaultencoding('utf-8')解决python2.7ascii编码问题
'''
reload(sys)
sys.setdefaultencoding('utf-8')
try:
    import xlrd
except:
    os.system('pip install -U xlrd')
    import xlrd
try:
    import requests
except ImportError as e:
    os.system('pip install -U requests')
    from pyDes import *
import smtplib  
from email.mime.text import MIMEText 

log_file = os.path.join(os.getcwd(),'log/liveappapi.log')
log_format = '[%(asctime)s] [%(levelname)s] %(message)s'
# 第一步，创建一个logger
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)    # Log等级总开关

fh = logging.FileHandler(log_file, mode='w')
fh.setLevel(logging.DEBUG)   # 输出到file的log等级的开关

# 第三步，再创建一个handler，用于输出到控制台
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)   # 输出到console的log等级的开关

# 第四步，定义handler的输出格式
formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
fh.setFormatter(formatter)
ch.setFormatter(formatter)

# 第五步，将logger添加到handler里面
logger.addHandler(fh)
logger.addHandler(ch)
#获取并执行测试用例
errorCase = []
def runTest(testCaseFile):
    '''
    作者：赵华兵
    时间: 2017-12-7
    功能: 执行 testCaseFile 的 所有测试案例
    '''
    testCaseFile = os.path.join(os.getcwd(),testCaseFile)
    if not os.path.exists(testCaseFile):
        logging.error('测试用例文件不存在！！！')
        sys.exit()
    testCase = xlrd.open_workbook(testCaseFile,encoding_override="cp1252")
    table = testCase.sheet_by_index(0)

    correlationDict = {}
    for i in range(1,table.nrows):
        if table.cell(i,10).value.replace('\n','').replace('\r','') != 'Yes':
            continue
        num = str(int(table.cell(i,0).value)).replace('\n','').replace('\r','')
        api_purpose = table.cell(i,1).value.replace('\n','').replace('\r','').encode('utf-8')
        api_host = table.cell(i,2).value.replace('\n','').replace('\r','')
        request_url = table.cell(i,3).value.replace('\n','').replace('\r','')
        request_method = table.cell(i,4).value.replace('\n','').replace('\r','').encode('utf-8')
        request_data_type = table.cell(i,5).value.replace('\n','').replace('\r','')
        request_data = table.cell(i,6).value.replace('\n','').replace('\r','')
        Category = table.cell(i,7).value.replace('\n','').replace('\r','').encode('utf-8')
        check_point = table.cell(i,8).value.encode('utf-8')#replace('\n','').replace('\r','')
        correlation = table.cell(i,9).value.replace('\n','').replace('\r','').split(';')

        if request_data_type == 'Form':
            ''' 将xlsx中request_data 'unicode'编码转化成 dict类型'''
            request_data_new=json.loads(request_data.encode('utf-8'))

        status, response = interfaceTest(num=num,api_purpose=api_purpose,api_host=api_host, request_url=request_url, request_data=request_data_new,request_method=request_method, check_point=check_point,request_data_type=request_data_type,Category=Category,correlation=correlation)
        if status != 200:
            check_point_str='无'
            errorCase.append(( num + ' ' + api_purpose, str(status), 'http://' + api_host + request_url,check_point_str+"," +'请求参数='+request_data.encode('utf-8'),response))
#         for key in correlationDict:
#             if request_url.find(key) > 0:
#                 request_url = request_url.replace(key,str(correlationDict[key]))

#             if os.path.exists(dataFile):
#                 fopen = open(dataFile,encoding='utf-8')
#                 request_data = fopen.readline()
#                 fopen.close()
#             for keyword in correlationDict:
#                 if request_data.find(keyword) > 0:
#                     request_data = request_data.replace(keyword,str(correlationDict[keyword]))
#
#                 else:
#                     request_data = urlencode(json.loads(request_data))
#             except Exception as e:
#                 logging.error(num + ' ' + api_purpose + ' 请求的数据有误，请检查[Request Data]字段是否是标准的json格式字符串！')
#                 continue
#         elif request_data_type == 'Data':
#             dataFile = request_data
#             if os.path.exists(dataFile):
#                 fopen = open(dataFile,encoding='utf-8')
#                 request_data = fopen.readline()
#                 fopen.close()
#             for keyword in correlationDict:
#                 if request_data.find(keyword) > 0:
#                     request_data = request_data.replace(keyword,str(correlationDict[keyword]))
#             request_data = request_data.encode('utf-8')
#         elif request_data_type == 'File':
#             dataFile = request_data
#             if not os.path.exists(dataFile):
#                 logging.error(num + ' ' + api_purpose + ' 文件路径配置无效，请检查[Request Data]字段配置的文件路径是否存在！！！')
#                 continue
#             fopen = open(dataFile,'rb')
#             data = fopen.read()
#             fopen.close()
#             request_data = '''
# ------WebKitFormBoundaryDf9uRfwb8uzv1eNe
# Content-Disposition:form-data;name="file";filename="%s"
# Content-Type:
# Content-Transfer-Encoding:binary
#
# %s
# ------WebKitFormBoundaryDf9uRfwb8uzv1eNe--
#     ''' % (os.path.basename(dataFile),data)
#         status,resp = interfaceTest(num,api_purpose,api_host,request_url,request_data,check_point,request_method,request_data_type)

#             continue
#         for j in range(len(correlation)):
#             param = correlation[j].split('=')
#             if len(param) == 2:
#                 if param[1] == '' or not re.search(r'^\[',param[1]) or not re.search(r'\]$',param[1]):
#                     logging.error(num + ' ' + api_purpose + ' 关联参数设置有误，请检查[Correlation]字段参数格式是否正确！！！')
#                     continue
#                 value = resp
#                 for key in param[1][1:-1].split(']['):
#                     try:
#                         temp = value[int(key)]
#                     except:
#                         try:
#                             temp = value[key]
#                         except:
#                             break
#                     value = temp
#                 correlationDict[param[0]] = value
    return errorCase


# 接口测试
def interfaceTest(num,api_purpose,api_host,request_url,request_data,check_point,request_method,request_data_type,Category,correlation):
    '''
    作者：赵华兵
    时间: 2017-12-7
    功能: 实现http接口请求方法，参数==>> 和.xlsx表格数据对应!
    '''
    #截取cookie
    cookie_list=[]
    if Category == "boss":
        cookie_value=cookie("boss")
        cookie_list.append(cookie_value)
    elif Category == "mch":
        cookie_value = cookie("mch")
        cookie_list.append(cookie_value)
    if len(cookie_list) != 0:
        Cookie = "X-Nova-Token=%s"%cookie_list[0]
    else:
        Cookie =""

    headers = {"Content-Type":"application/json",
               'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36',
               'Cookie': Cookie,
               }
    request_url_new = 'http://' + api_host + request_url
    data=json.dumps(request_data)

    if request_method == "POST":
        response_info = requests.post(url=request_url_new,data=data,headers=headers)
    elif request_method == "GET":
        response_info = requests.get(url=request_url_new,headers=headers)
    else:
        logging.error(num + ' ' + api_purpose + ' HTTP请求方法错误，请确认[Request Method]字段是否正确！！！')
    response = response_info.text
    status = response_info.status_code
    #状态码判断
    if status == 200:
        resp = response.encode('utf-8')
        if re.search(check_point,resp):
            logging.info(num + ' ' + api_purpose + ' 成功, ' + str(status) + ', '+resp)
            return status,json.loads(resp)
        else:
            logging.error(num + ' ' + api_purpose + ' 失败！！！, [ ' + str(status) + ' ], '+ resp)
            errorCase.append((num + ' ' + api_purpose, str(status), 'http://' + api_host + request_url,check_point +"," +'请求参数='+str(request_data).encode('utf-8') ,response))
            return status,resp
    else:
        logging.error(num + ' ' + api_purpose + ' 失败！！！, [ ' + str(status) + ' ], ' + response)
        return status,response
    return

def cookie(Category):
    '''
        作者：赵华兵
        时间: 2017-12-11
        功能: 获取对应的cookie信息!  boss =运营中心， mch=商户中心
        '''
    headers = {'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
               'X-Requested-With': 'XMLHttpRequest',
               'Connection': 'keep-alive',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36'
               }
    if Category == "boss":
        url='http://cpcr.novaszco.com/gateway/boss/user/login'
        data = {"username": "admin001",
                "password": "admin001"}
        cookie_response = requests.post(url=url, headers=headers, data=data)

    elif Category =="mch":
        url = 'http://cpcr.mch.novaszco.com/api/user/login'
        data = {"username": "admin001",
                "password": "admin001"}
        cookie_response = requests.post(url=url, headers=headers, data=data)

    return cookie_response.cookies.get_dict()['X-Nova-Token']

#发送通知邮件
def sendMail(text):
    sender = '13823720073@163.com'
    #收件人邮箱，，可设置多个
    receiver = ['13823720073@163.com',]#"wenjianhua@novaszco.com"
    # 抄送人
    mailToCc = ['13823720073@163.com']
    subject = '[AutomantionTest]接口自动化测试报告通知'  
    smtpserver = 'smtp.163.com'
    username = '13823720073@163.com'
    password = 'zhao12'
    
    msg = MIMEText(text,'html','utf-8')      
    msg['Subject'] = subject  
    msg['From'] = sender
    msg['To'] = ';'.join(receiver)
    msg['Cc'] = ';'.join(mailToCc)
    smtp = smtplib.SMTP()  
    smtp.connect(smtpserver)  
    smtp.login(username, password)  
    smtp.sendmail(sender, receiver + mailToCc, msg.as_string())  
    smtp.quit() 

def main(Casepath):
    errorTest = runTest(Casepath)

    if len(errorTest) > 0:

        html = '<html><body><p>接口自动化定期扫描，共有 ' + str(len(errorTest)) + ' 个异常接口，列表如下：' + '</p><table style="border: 1px solid black;"><tr style="background: green;"><th style="width:100px;">接口编号</th><th style="width:50px;">状态</th><th style="width:200px;">接口地址</th><th style="width:50px;">断言及校验参数</th><th thstyle="width:50px;">返回结果</th></tr>'
        for test in errorTest:
            # print test
            html = html + '<tr style="background: grey"><td style="padding: 10px;"><h5>' + test[0] + '</td></h5><td style="padding: 10px;">' + test[1] + '</td><td style="padding: 10px;">' + test[2] + '</td><td style="padding: 10px;">' + test[3] + '</td><td style="padding: 10px;">' + test[4] + '</td></tr>'
        html = html + '</table></body></html>'
        sendMail(html)


