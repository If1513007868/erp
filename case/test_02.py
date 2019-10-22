import unittest
import time
import requests
from case.login_bzj import refreshToken

#模块调用token的方法
# test = Blog_login()
# res = test.log(15130078689, 123456)
# refreshToken = res['result']['token']

# data = {"pageNum":"1","pageSize":"40",}
# url = "http://172.16.20.152:7040/api/ec/user/auth/getContactList"
# hearders= {
#
#     "Authorization":refreshToken
# }
#
# r = requests.get(url,data,headers=hearders)
# print(r.status_code)
# print(r.json())

class Obtain_Contact(unittest.TestCase):
    #获取联系人列表
    def test_contact_list(self):
        url = "http://172.16.20.152:7040/api/ec/user/auth/getContactList"
        data = {"pageNum": "1", "pageSize": "40", }
        hearders = {

            "Authorization": refreshToken
        }
        res = requests.get(url, data, headers=hearders)
        res.content.decode('utf-8')
        print(res.json())
        return res.json()

#校验联系人信息
    def test_check_contact(self):
        result = self.test_contact_list()
        #获取联系人总数
        total = result["result"]["total"]
        print(result["result"]["data"][0]["name"])
        self.assertEqual(result["code"],'100100')
        self.assertEqual(result["msg"], '联系人获取成功')
        self.assertEqual(result["result"]["pageNum"], 1)
        self.assertEqual(result["result"]["pageSize"], 40)
        self.assertEqual(result["result"]["total"],total)
        self.assertEqual(result["result"]["data"][0]["cardNo"],'13013319930311093X')
        self.assertEqual(result["result"]["data"][0]["birthday"], 731779200000)




if __name__ == "__main__":
    unittest.main()


