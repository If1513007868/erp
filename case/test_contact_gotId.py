#/user/auth/getContactList  校验联系人信息
import unittest
import requests
from case.login_bzj import host
from case.login_bzj import getToken
class check_contact(unittest.TestCase):

    hearders = {

        "Authorization": getToken
    }
#根据ID获取联系人
    def test_getId(self):
        u'''根据ID获取联系人'''
        url = host+"user/auth/getContactById"
        data = {"id": "478" }
        res = requests.get(url, data, headers=self.hearders)
        res.content.decode('utf-8')
        result = res.json()

    # 打印联系人列表
        #print(res.json())

    # 检验联系人是否获取成功
        self.assertEqual(result["code"], '100100')
        self.assertEqual(result["msg"], '联系人获取成功')

    # 检验联系人数据是否正确

        self.assertEqual(result["result"]["name"], '保之家')
        self.assertEqual(result["result"]["cardNo"], '13013319930311093X')
        self.assertEqual(result["result"]["birthday"], 731779200000)
        self.assertEqual(result["result"]["englishName"], 'baobao')
        self.assertEqual(result["result"]["cardType"], 'IDENTITY')
        self.assertEqual(result["result"]["phone"], '15130000001')
        self.assertEqual(result["result"]["zipCode"], '051530')
        self.assertEqual(result["result"]["mail"], '756016656@qq.com')
        self.assertEqual(result["result"]["sex"], 1)
        self.assertEqual(result["result"]["address"], '北京市北京经济技术开发区荣华中路8号院4号楼11层1102')

        return res.json()
#根据ID获取联系人(id为空)
    def test_getId1(self):
        u'''根据ID获取联系人(id为空)'''
        url = host+"user/auth/getContactById"
        data = {"id": "" }
        res = requests.get(url, data, headers=self.hearders)
        res.content.decode('utf-8')
        result = res.json()

        # 检验联系人是否获取成功
        self.assertEqual(result["code"], '400 BAD_REQUEST')
        self.assertEqual(result["msg"], '缺少参数!')
#缺少token)
    def test_getId2(self):
        u'''缺少token)'''
        url = host+"user/auth/getContactById"
        data = {"id": "" }
        res = requests.get(url, data)
        res.content.decode('utf-8')
        result = res.json()
        print(result)

        # 检验联系人是否获取成功
        self.assertEqual(result["code"], '403012')
        self.assertEqual(result["msg"], '非授权访问，无效的token')




if __name__ == "__main__":
    unittest.main()

