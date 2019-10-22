import unittest
import requests
from case.login_bzj import host
from case.login_bzj import refreshToken
class check_contact(unittest.TestCase):

    hearders = {

        "Authorization": refreshToken
    }
    def test_getId(self):
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



if __name__ == "__main__":
    unittest.main()

