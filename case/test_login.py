#Python 报错    导入urllib3    urllib3.disable_warnings()
#验证登录

import unittest
from case.login_bzj import Bzj_login
class Verify_login(unittest.TestCase):
    ver = Bzj_login()

#1.正确的账号密码

    def test_login1(self):
        u'''登录用例，正确账号密码'''
        phone = "15130078689"
        credential = "123456"
        result = self.ver.login(phone,credential)
        # 在调用函数后打印返回值
        # print(result)
        self.assertEqual(result["code"], '100100')
        self.assertEqual(result["msg"],'请求成功' )
        self.assertEqual(result["result"]["phone"],"15130078689")

#2.账号正确，密码错误
    def test_login2(self):
        u'''登录用例，账号正确，密码错误'''
        phone = "15130078689"
        credential = "1234567123"
        result = self.ver.login(phone, credential)
        self.assertEqual(result["code"], '403006')
        self.assertEqual(result["msg"], '账号或密码错误')

#3.账号错误
    def test_login3(self):
        u'''登录用例，账号正确，密码错误'''
        phone = "1513078689"
        credential = "123456"
        result = self.ver.login(phone, credential)
        self.assertEqual(result["code"], '403001')
        self.assertEqual(result["msg"], '用户不存在!')

#4.账号密码错误
    def test_login4(self):
        u'''登录用例，账号密码错误'''
        phone = "151307868"
        credential = "12345"
        result = self.ver.login(phone, credential)
        self.assertEqual(result["code"], '403001')
        self.assertEqual(result["msg"], '用户不存在!')

# 4.账号密码为空
    def test_login5(self):
        u'''登录用例，账号密码为空'''
        phone = ""
        credential = ""
        result = self.ver.login(phone, credential)
        self.assertEqual(result["code"], '401002')
        self.assertEqual(result["msg"], '参数为空')

# 4.账号密码为空
    def test_login6(self):
        u'''登录用例，账号密码为空'''
        phone = ""
        credential = "123456"
        result = self.ver.login(phone, credential)

        self.assertEqual(result["code"], '401002')
        self.assertEqual(result["msg"], '参数为空')

# 4.账号密码为空
    def test_login7(self):
        u'''登录用例，账号密码为空'''
        phone = ""
        credential = ""
        result = self.ver.login(phone, credential)
        self.assertEqual(result["code"], '401002')
        self.assertEqual(result["msg"], '参数为空')




#其他模块调用这个token变量
# test = Blog_login()
# res = test.log(15130078689, 123456)
# refreshToken = res['result']['token']
# print(refreshToken)

if __name__ == "__main__":
    unittest.main()


