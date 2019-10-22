import unittest
from case.contact_list import Obtain_Contact
class check_contact(unittest.TestCase):
    check = Obtain_Contact()

# 校验联系人知否正确信息
    def test_check_contact(self):
        u'''校验联系人知否正确信息'''

        result = self.check.test_contact_list()
        #获取联系人总数
        total = result["result"]["total"]
        self.assertEqual(result["result"]["total"], total)

        #print(result["result"]["data"][0]["name"])
#检验联系人是否获取成功
        self.assertEqual(result["code"], '100100')
        self.assertEqual(result["msg"], '联系人获取成功')
# 检验联系人数据是否正确
        self.assertEqual(result["result"]["pageNum"], 1)
        self.assertEqual(result["result"]["pageSize"], 40)
        self.assertEqual(result["result"]["data"][0]["name"], '保之家')
        self.assertEqual(result["result"]["data"][0]["cardNo"],'13013319930311093X')
        self.assertEqual(result["result"]["data"][0]["birthday"], 731779200000)
        self.assertEqual(result["result"]["data"][0]["englishName"], 'baobao')
        self.assertEqual(result["result"]["data"][0]["cardType"], 'IDENTITY')
        self.assertEqual(result["result"]["data"][0]["phone"], '15130000001')
        self.assertEqual(result["result"]["data"][0]["zipCode"], '051530')
        self.assertEqual(result["result"]["data"][0]["mail"], '756016656@qq.com')
        self.assertEqual(result["result"]["data"][0]["sex"], 1)
        self.assertEqual(result["result"]["data"][0]["address"], '北京市北京经济技术开发区荣华中路8号院4号楼11层1102')


if __name__ == "__main__":
    unittest.main()