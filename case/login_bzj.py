
import unittest
import requests

host ='http://172.16.20.152:7040/api/ec/'

#定义一个全局变量
# def text():
#     global host
#     host = "C语言中文网"
#     print("函数体内访问：", host)
#text()
print('函数体外访问：', host)

class Bzj_login(unittest.TestCase):





    def login(self,phone,credential):
        url = host+'login'
        hearders = {

            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:68.0) Gecko/20100101 Firefox/68.0",
            "Accept": "*/*",
            "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
            "Accept-Encoding": "gzip, deflate",
            "Content-Type": "application/json;charset=utf-8",
            "Content-Length": "63",
            "Connection": "keep-alive"

        }
        payload = {

            "credential": credential,
            "phone": phone,
            "type": "PASSWARD"
        }
        res = requests.post(url,headers=hearders,json=payload)
        #print(res.content.decode('utf-8'))  #将英文转化成汉字
        return res.json()

#获取token
test = Bzj_login()
res = test.login(15130078689, 123456)
refreshToken = res['result']['token']

if __name__ == "__main__":
    unittest.main()