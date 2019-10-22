import unittest
from HTMLTestRunner import HTMLTestRunner
#3.新建一个HTMLTestRunner文件夹，并在文件夹下新建一个空的__init__.py文件，这样文件夹HTMLTestRunner就变成了一个可以导入的包，然后将HTMLTestRunner.py也放入文件夹里。

def all_case():
    # 待执行用例的目录
    case_dir = "/Users/mac/Desktop/test_yo/case"
    testcase = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(case_dir,pattern="test*.py",top_level_dir=None)

#discover筛选出所有用例，循环添加到测试套件中
    for test_suite in discover:
        for test_case in test_suite:
            testcase.addTests(test_case)
        #添加测试用例
        #testcase.addTests(test_case)

    print(testcase)
    return testcase
if __name__ == "__main__":
    #返回实例
    #runner = unittest.TextTestRunner()
    #run所有用例
    #runner.run(all_case())

    report_path = "/Users/mac/Desktop/test_yo/report/result.html"
    fp = open(report_path,"wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title=u"我的自动化测试报告",description=u'用例执行情况：')
    runner.run(all_case())
    fp.close()

