import unittest
import requests
from case.login_bzj import host
from case.login_bzj import refreshToken

class ModifyPassword(unittest.TestCase):
    hearders = {

        "Authorization": refreshToken
    }
# 更换手机号身份验证（密码）
    def test_modpwd(self):
        u'''更换手机号身份验证（密码）'''
        url = host + "user/auth/replaceVerify"
        data = {"password": "123456","type": "password"}
        res = requests.post(url, data, headers=self.hearders)
        res.content.decode('utf-8')
        result = res.json()
        # 打印联系人列表
        # print(res.json())

        # 检验联系人是否获取成功
        self.assertEqual(result["code"], '100100')
        self.assertEqual(result["msg"], '验证成功')

# 更换手机号身份验证（密码为空）
    def test_modpwd1(self):
        u'''更换手机号身份验证（密码密码为空）'''
        url = host + "user/auth/replaceVerify"
        data = {"password": "","type": "password"}
        res = requests.post(url, data, headers=self.hearders)
        res.content.decode('utf-8')
        result = res.json()
        # 打印联系人列表
        # print(res.json())

        # 检验联系人是否获取成功
        self.assertEqual(result["code"], '500 INTERNAL_SERVER_ERROR')
        self.assertEqual(result["msg"], '服务错误，请稍后重试！（null）')

# 更换手机号身份验证（密码不正确）
    def test_modpwd2(self):
        u'''更换手机号身份验证（密码不正确）'''
        url = host + "user/auth/replaceVerify"
        data = {"password": "1234","type": "password"}
        res = requests.post(url, data, headers=self.hearders)
        res.content.decode('utf-8')
        result = res.json()
        # 打印联系人列表
        # print(res.json())

        # 检验联系人是否获取成功
        self.assertEqual(result["code"], '403002')
        self.assertEqual(result["msg"], '密码不匹配,禁止操作')
# 更换手机号身份验证（手机号）
    def test_modpwd3(self):
        u'''更换手机号身份验证（手机号）'''
        url = host + "user/auth/replaceVerify"
        data = {"phone": "15130078689","type": "phone","vcode": "7779"}
        res = requests.post(url, data, headers=self.hearders)
        res.content.decode('utf-8')
        result = res.json()
        # 打印联系人列表
        #print(res.json())

        # 检验联系人是否获取成功
        self.assertEqual(result["code"], '100100')
        self.assertEqual(result["msg"], '验证成功')

# 更换手机号身份验证（手机号为空）
    def test_modpwd4(self):
        u'''更换手机号身份验证（手机号为空）'''
        url = host + "user/auth/replaceVerify"
        data = {"phone": "","type": "phone","vcode": "7779"}
        res = requests.post(url, data, headers=self.hearders)
        res.content.decode('utf-8')
        result = res.json()
        # 打印联系人列表
        #print(res.json())

        # 检验联系人是否获取成功
        self.assertEqual(result["code"], '400 BAD_REQUEST')
        self.assertEqual(result["msg"], '缺少参数!')

# 更换手机号身份验证（手机号不正确）
    def test_modpwd5(self):
        u'''更换手机号身份验证（手机号不正确）'''
        url = host + "user/auth/replaceVerify"
        data = {"phone": "1513000001","type": "phone","vcode": ""}
        res = requests.post(url, data, headers=self.hearders)
        res.content.decode('utf-8')
        result = res.json()
        # 打印联系人列表
        #print(res.json())

        # 检验联系人是否获取成功
        self.assertEqual(result["code"], '405001')
        self.assertEqual(result["msg"], '手机号码不正确')

# 更换手机号身份验证（验证码为空）
    def test_modpwd6(self):
        u'''更换手机号身份验证（手机号不正确）'''
        url = host + "user/auth/replaceVerify"
        data = {"phone": "15130078689","type": "phone","vcode": ""}
        res = requests.post(url, data, headers=self.hearders)
        res.content.decode('utf-8')
        result = res.json()
        # 打印联系人列表
        #print(res.json())

        # 检验联系人是否获取成功
        self.assertEqual(result["code"], '400 BAD_REQUEST')
        self.assertEqual(result["msg"], '缺少参数!')
# 更换手机号身份验证（验证码不正确）
    def test_modpwd7(self):
        u'''更换手机号身份验证（手机号不正确）'''
        url = host + "user/auth/replaceVerify"
        data = {"phone": "15130078689","type": "phone","vcode": "123"}
        res = requests.post(url, data, headers=self.hearders)
        res.content.decode('utf-8')
        result = res.json()
        # 打印联系人列表
        #print(res.json())

        # 检验联系人是否获取成功
        self.assertEqual(result["code"], '403006')
        self.assertEqual(result["msg"], '短信验证码不正确')

if __name__ == "__main__":
    unittest.main()