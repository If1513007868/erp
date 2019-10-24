#/user/auth/modifyPassword修改密码

import unittest
import requests
from case.login_bzj import host
from case.login_bzj import getToken

class ModifyPassword(unittest.TestCase):
    hearders = {

        "Authorization": getToken
    }
# 修改密码
    def test_modpwd(self):
        u'''修改密码'''
        url = host + "user/auth/modifyPassword"
        data = {"oldPassword": "123456","newPassword": "123456"}
        res = requests.post(url, data, headers=self.hearders)
        res.content.decode('utf-8')
        result = res.json()
        # 打印联系人列表
        # print(res.json())

        # 检验联系人是否获取成功
        self.assertEqual(result["code"], '100100')
        self.assertEqual(result["msg"], '密码修改成功')

# 没有token
    def test_modpwdtoken(self):
        u'''没有token'''
        url = host + "user/auth/modifyPassword"
        data = {"oldPassword": "123456", "newPassword": "123456"}
        res = requests.post(url, data)
        res.content.decode('utf-8')
        result = res.json()
        # 打印联系人列表
        #print(res.json())

        # 检验联系人是否获取成功
        self.assertEqual(result["code"], '403012')
        self.assertEqual(result["msg"], '非授权访问，无效的token')

#原密码不正确
    def test_modpwd1(self):
        u'''原密码不正确'''
        url = host + "user/auth/modifyPassword"
        data = {"oldPassword": "1234567","newPassword": "123456"}
        res = requests.post(url, data, headers=self.hearders)
        res.content.decode('utf-8')
        result = res.json()
        # 打印联系人列表
        #print(res.json())

        #检验联系人是否获取成功
        self.assertEqual(result["code"], '403002')
        self.assertEqual(result["msg"], '原密码不正确')
#新旧密码为空
    def test_modpwd2(self):
        u'''新旧密码为空'''
        url = host + "user/auth/modifyPassword"
        data = {" ": "","": ""}
        res = requests.post(url, data, headers=self.hearders)
        res.content.decode('utf-8')
        result = res.json()
        # 打印联系人列表
        #print(res.json())

    #检验联系人是否获取成功
        self.assertEqual(result["code"], '400 BAD_REQUEST')
        self.assertEqual(result["msg"], '缺少参数!')
#旧密码为空
    def test_modpwd3(self):
        u'''旧密码为空'''
        url = host + "user/auth/modifyPassword"
        data = {" ": "","newPassword":"123456"}
        res = requests.post(url, data, headers=self.hearders)
        res.content.decode('utf-8')
        result = res.json()
        # 打印联系人列表
        #print(res.json())

    #检验联系人是否获取成功
        self.assertEqual(result["code"], '400 BAD_REQUEST')
        self.assertEqual(result["msg"], '缺少参数!')
#新密码为空
    def test_modpwd4(self):
        u'''旧密码为空'''
        url = host + "user/auth/modifyPassword"
        data = {"oldPassword": "123456","":""}
        res = requests.post(url, data, headers=self.hearders)
        res.content.decode('utf-8')
        result = res.json()
        # 打印联系人列表
        #print(res.json())

    #检验联系人是否获取成功
        self.assertEqual(result["code"], '400 BAD_REQUEST')
        self.assertEqual(result["msg"], '缺少参数!')


if __name__ == "__main__":
    unittest.main()