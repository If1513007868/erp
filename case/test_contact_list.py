#/user/auth/getContactList 获取常用联系人列表
#/user/auth/addContact 添加常用联系人
#/user/auth/deleteContactById 根据id删除常用联系人

import unittest
import requests
import random
from case.login_bzj import host
from case.login_bzj import getToken




class Obtain_Contact(unittest.TestCase):
    #获取联系人列表

    hearders = {

        "Authorization": getToken
    }
#获取联系人列表
    def test_contact_list(self):
        u'''获取联系人列表'''
        url = host+"user/auth/getContactList"
        data = {"pageNum": "1", "pageSize": "40", }
        res = requests.get(url, data, headers=self.hearders)
        res.content.decode('utf-8')
        result = res.json()
    #打印联系人列表
        #print(res.json())
    # 检验联系人是否获取成功
        self.assertEqual(result["code"], '100100')
        self.assertEqual(result["msg"], '联系人获取成功')
    #获取联系人Id(第一个，删除用)
        self.get_id = (result["result"]["data"][1]["id"])


        return res.json()

#添加联系人
    def test_addcontact(self):
        u'''添加联系人列表'''
        url = host + "user/auth/addContact"

    #随机取身份证号
        foo = ['110101199003070679', '110101199003075250', '110101199003074696', '110101199003070054', '110101199003077299']
        cardNo = random.choice(foo)

    # 随机取姓名
        roo = ['测试一','测试二','测试三','测试四','测试五']
        name = random.choice(roo)

        payload = {

            "address": "北京市北京经济技术开发区荣华中路8号院4号楼11层1102",
            "birthday": "2019-10-21T08:47:54.523Z",
            "cardNo": cardNo,
            "cardType": "IDENTITY",
            "city": "3",
            "englishName": "baobao",
            "id": 0,
            "mail": "756016656@qq.com",
            "name": name,
            "phone": "15130078689",
            "province": "2",
            "relation": "SELF",
            "sex": 1,
            "userId": 0,
            "zipCode": "051530"
        }
        res = requests.post(url,json=payload, headers=self.hearders)
        res.content.decode('utf-8')
        result = res.json()
        #print(res.json())

    # 检验联系人是否添加成功
        self.assertEqual(result["code"], '100100')
        self.assertEqual(result["msg"], '添加常用联系人成功')
        return res.json()
#添加联系人列表(token为空)
    def test_addcontact_k(self):
        u'''添加联系人列表(token为空)'''
        url = host + "user/auth/addContact"

    #随机取身份证号
        foo = ['110101199003070679', '110101199003075250', '110101199003074696', '110101199003070054', '110101199003077299']
        cardNo = random.choice(foo)

    # 随机取姓名
        roo = ['测试一','测试二','测试三','测试四','测试五']
        name = random.choice(roo)

        payload = {

            "address": "北京市北京经济技术开发区荣华中路8号院4号楼11层1102",
            "birthday": "2019-10-21T08:47:54.523Z",
            "cardNo": cardNo,
            "cardType": "IDENTITY",
            "city": "3",
            "englishName": "baobao",
            "id": 0,
            "mail": "756016656@qq.com",
            "name": name,
            "phone": "15130078689",
            "province": "2",
            "relation": "SELF",
            "sex": 1,
            "userId": 0,
            "zipCode": "051530"
        }
        res = requests.post(url,json=payload)
        res.content.decode('utf-8')
        result = res.json()
        #print(res.json())

    # 检验联系人是否添加成功
        self.assertEqual(result["code"], '403012')
        self.assertEqual(result["msg"], '非授权访问，无效的token')
        return res.json()

#删除联系人

    def test_delcontact(self):
        u'''删除联系人'''

    #得到联系人Id
        self.test_contact_list()
        Id = self.get_id

        url = host + "/user/auth/deleteContactById"
        data = {"id":Id }
        res = requests.delete(url,params=data,headers=self.hearders)
        res.content.decode('utf-8')
        result = res.json()
        #print(res.json())
        self.assertEqual(result["code"], '100100')
        self.assertEqual(result["msg"], '删除联系人成功')

#删除联系人（Id为空

    def test_delcontact1(self):
        u'''删除联系人（Id为空）'''

    #得到联系人Id
        #self.test_contact_list()
        #Id = self.get_id

        url = host + "/user/auth/deleteContactById"
        data = {"id":"" }
        res = requests.delete(url,params=data,headers=self.hearders)
        res.content.decode('utf-8')
        result = res.json()
        #print(res.json())
        self.assertEqual(result["code"], '400 BAD_REQUEST')
        self.assertEqual(result["msg"], '缺少参数!')

#删除已删除的联系人

    def test_delcontact2(self):
        u'''删除已删除的联系人'''
        url = host + "/user/auth/deleteContactById"
        data = {"id": "495"}
        res = requests.delete(url,params=data,headers=self.hearders)
        res.content.decode('utf-8')
        result = res.json()
        #print(res.json())
        self.assertEqual(result["code"], '406001')
        self.assertEqual(result["msg"], '删除联系人失败')

#删除联系人（token为空）
    def test_delcontact4(self):
        u'''删除联系人（token为空）'''

    #得到联系人Id
        self.test_contact_list()
        Id = self.get_id

        url = host + "/user/auth/deleteContactById"
        data = {"id":Id }
        res = requests.delete(url,params=data)
        res.content.decode('utf-8')
        result = res.json()
        #print(res.json())
        self.assertEqual(result["code"], '403012')
        self.assertEqual(result["msg"], '非授权访问，无效的token')








if __name__ == "__main__":
    unittest.main()