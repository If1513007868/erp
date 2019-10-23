#/user/auth/getUserInfo   获取用户信息


import unittest
import requests
from case.login_bzj import host
from case.login_bzj import refreshToken

class Get_Userinfo(unittest.TestCase):
#根据ID获取用户信息
    def test_getuser(self):
        u'''根据ID获取用户信息'''
        data = {"id": "45"}
        hearders = {

            "Authorization": refreshToken
        }
        url = host + "user/auth/getUserInfo"
        res = requests.get(url, data, headers=hearders)
        res.content.decode('utf-8')
        result = res.json()
        print(res.json())

    #检验用户信息是否获取成功
        self.assertEqual(result["code"], '100100')
        self.assertEqual(result["msg"], '请求成功')
    #检验用户信息
        self.assertEqual(result["result"]["id"], 45)
        self.assertEqual(result["result"]["name"], '路飞')
        self.assertEqual(result["result"]["nickname"], '15130078689')
        self.assertEqual(result["result"]["realname"], '李亮')
        self.assertEqual(result["result"]["address"], '河北石家庄市赵县北王里镇北王里村6巷2号')
        self.assertEqual(result["result"]["mail"], '15130078689@163.com')

        return res.json()

#ID为空

    def test_getuser1(self):
        #请求到500是因为url把id加到后面传进去了，造成链接是错了
        u'''ID为空'''
        data = {"":""}
        hearders = {

            "Authorization": refreshToken
        }
        url = host + "user/auth/getUserInfo"
        res = requests.get(url, data, headers=hearders)
        res.content.decode('utf-8')
        result = res.json()
        #print(res.json())

    #检验用户信息是否获取成功
        self.assertEqual(result["code"], '400 BAD_REQUEST')
        self.assertEqual(result["msg"], '缺少参数!')

#token为空
    def test_getuser2(self):
        u'''token为空'''

        data = {"id":"45"}
        url = host + "user/auth/getUserInfo"
        res = requests.get(url, data)
        res.content.decode('utf-8')
        result = res.json()
        #print(res.json())

    #检验用户信息是否获取成功
        self.assertEqual(result["code"], '403012')
        self.assertEqual(result["msg"], '非授权访问，无效的token')




if __name__ == "__main__":
    unittest.main()