import unittest
import requests
from case.login_bzj import host
from case.login_bzj import getToken


class Send_MailVCode(unittest.TestCase):
    hearders = {

        "Authorization": getToken
    }
#发送邮箱验证码
    def test_mailvcode(self):
        u'''发送邮箱验证码'''
        url = host + "user/auth/sendMailVCode"
        data = {"mail": "15130078689@163.com"}
        res = requests.post(url, data, headers=self.hearders)
        res.content.decode('utf-8')
        result = res.json()

        # 打印联系人列表
        # print(res.json())

        # 检验联系人是否获取成功
        self.assertEqual(result["code"], '100100')
        self.assertEqual(result["msg"], '发送验证码成功')

#发送邮箱验证码（没有token）
    def test_mailvcode1(self):
        u'''发送邮箱验证码没有token）'''
        url = host + "user/auth/sendMailVCode"
        data = {"mail": "15130078689@163.com"}
        res = requests.post(url, data)
        res.content.decode('utf-8')
        result = res.json()

        # 打印联系人列表
        #print(res.json())

        # 检验联系人是否获取成功
        self.assertEqual(result["code"], '403012')
        self.assertEqual(result["msg"], '非授权访问，无效的token')

#发送邮箱验证码（邮箱为空）
    def test_mailvcode2(self):
        u'''发送邮箱验证码邮箱为空）'''
        url = host + "user/auth/sendMailVCode"
        data = {"mail": ""}
        res = requests.post(url, data, headers=self.hearders)
        res.content.decode('utf-8')
        result = res.json()

        # 打印联系人列表
        #print(res.json())

        # 检验联系人是否获取成功
        self.assertEqual(result["code"], '401002')
        self.assertEqual(result["msg"], '邮箱不能为空')


#发送邮箱验证码（邮箱格式错误）
    def test_mailvcode3(self):
        u'''发送邮箱验证码（邮箱格式错误）'''
        url = host + "user/auth/sendMailVCode"
        data = {"mail": "@163.com"}
        res = requests.post(url, data, headers=self.hearders)
        res.content.decode('utf-8')
        result = res.json()

        # 打印联系人列表
        #print(res.json())

        # 检验联系人是否获取成功
        self.assertEqual(result["code"], '500 INTERNAL_SERVER_ERROR')
        self.assertEqual(result["msg"], '服务错误，请稍后重试！（AddressException: Missing local name）')

# 发送邮箱验证码（邮箱参数为空）
    def test_mailvcode4(self):
        u'''发送邮箱验证码（邮箱参数为空）'''
        url = host + "user/auth/sendMailVCode"
        data = {"": ""}
        res = requests.post(url, data, headers=self.hearders)
        res.content.decode('utf-8')
        result = res.json()

        # 打印联系人列表
        #print(res.json())

        # 检验联系人是否获取成功
        self.assertEqual(result["code"], '400 BAD_REQUEST')
        self.assertEqual(result["msg"], '缺少参数!')

if __name__ == "__main__":
    unittest.main()
