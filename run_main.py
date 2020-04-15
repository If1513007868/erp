import unittest
from HTMLTestRunner import HTMLTestRunner
import os
import time

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
#3.新建一个HTMLTestRunner文件夹，并在文件夹下新建一个空的__init__.py文件，这样文件夹HTMLTestRunner就变成了一个可以导入的包，然后将HTMLTestRunner.py也放入文件夹里。


cur_path = os.path.dirname(os.path.realpath(__file__))
print(cur_path)
#旧的代码
# def all_case():
#     # 待执行用例的目录
#     #case_dir = "/Users/mac/Desktop/test_yo/case"
#     case_dir = "/Users/mac/Desktop/123/han/case"
#     testcase = unittest.TestSuite()
#     discover = unittest.defaultTestLoader.discover(case_dir,pattern="test*.py",top_level_dir=None)
#
# #discover筛选出所有用例，循环添加到测试套件中
#     for test_suite in discover:
#         for test_case in test_suite:
#             testcase.addTests(test_case)
#         #添加测试用例
#         #testcase.addTests(test_case)
#
#     print(testcase)
#     return testcase
# if __name__ == "__main__":
#     #返回实例
#     #runner = unittest.TextTestRunner()
#     #run所有用例
#     #runner.run(all_case())
#
#     #report_path = "/Users/mac/Desktop/test_yo/report/result.html"
#     report_path = "/Users/mac/Desktop/123/han/report/result.html"
#     fp = open(report_path,"wb")
#     runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title=u"我的自动化测试报告",description=u'用例执行情况：')
#     runner.run(all_case())
#     fp.close()

def add_case(caseName="case", rule="test*.py"):
    '''第一步：加载所有的测试用例'''
    case_path = os.path.join(cur_path, caseName)  # 用例文件夹
    # 如果不存在这个case文件夹，就自动创建一个
    if not os.path.exists(case_path):os.mkdir(case_path)
    print("test case path:%s"%case_path)
    # 定义discover方法的参数
    discover = unittest.defaultTestLoader.discover(case_path,pattern=rule,top_level_dir=None)
    print(discover)
    return discover

def run_case(all_case, reportName="report"):
    '''第二步：执行所有的用例, 并把结果写入HTML测试报告'''
    now = time.strftime("%Y_%m_%d_%H_%M_%S")
    report_path = os.path.join(cur_path, reportName)  # 用例文件夹
    # 如果不存在这个report文件夹，就自动创建一个
    if not os.path.exists(report_path):os.mkdir(report_path)
    report_abspath = os.path.join(report_path, now+"result.html")
    print("report path:%s"%report_abspath)
    fp = open(report_abspath, "wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                           title=u'自动化测试报告,测试结果如下：',
                                           description=u'用例执行情况：')

    # 调用add_case函数返回值
    runner.run(all_case)
    fp.close()

def get_report_file(report_path):
    '''第三步：获取最新的测试报告'''
    lists = os.listdir(report_path)
    lists.sort(key=lambda fn: os.path.getmtime(os.path.join(report_path, fn)))
    print (u'最新测试生成的报告： '+lists[-1])
    # 找到最新生成的报告文件
    report_file = os.path.join(report_path, lists[-1])
    return report_file

def send_mail(sender, psw, receiver, smtpserver, report_file, port):
    '''第四步：发送最新的测试报告内容'''
    with open(report_file, "rb") as f:
        mail_body = f.read()
    # 定义邮件内容
    msg = MIMEMultipart()
    body = MIMEText(mail_body, _subtype='html', _charset='utf-8')
    msg['Subject'] = u"自动化测试报告"
    msg["from"] = sender
    msg["to"] = psw
    msg.attach(body)
    # 添加附件
    att = MIMEText(open(report_file, "rb").read(), "base64", "utf-8")
    att["Content-Type"] = "application/octet-stream"
    att["Content-Disposition"] = 'attachment; filename= "report.html"'
    msg.attach(att)
    try:
        smtp = smtplib.SMTP_SSL(smtpserver, port)
    except:
        smtp = smtplib.SMTP()
        smtp.connect(smtpserver, port)
    # 用户名密码
    smtp.login(sender, psw)
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()
    print('test report email has send out !')




if __name__ == "__main__":
    all_case = add_case()   # 1加载用例
    # 生成测试报告的路径
    run_case(all_case)
    # 获取最新的测试报告文件
    report_path = os.path.join(cur_path, "report")  # 用例文件夹
    report_file = get_report_file(report_path)  # 3获取最新的测试报告
    # 邮箱配置
    from config import readConfig

    sender = readConfig.sender
    psw = readConfig.psw
    smtp_server = readConfig.smtp_server
    port = readConfig.port
    receiver = readConfig.receiver
    send_mail(sender, psw, receiver, smtp_server, report_file, port)  # 4最后一步发送报告

