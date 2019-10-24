import unittest
from case.login_bzj import Bzj_login
from common.logger import Log



class Verify_login(unittest.TestCase):
    ver = Bzj_login()
    log = Log()



#1.正确的账号密码

    def test_login1(self):

        u'''登录用例，正确账号密码'''
        self.log.info("===start====")
        phone = "15130078689"
        credential = "123456"
        result = self.ver.login(phone,credential)
        self.log.info(u'''调取登录结果：%s'''%result["msg"])
        # # 在调用函数后打印返回值
        #print(result)
        self.assertEqual(result["code"], '100100')
        # self.assertEqual(result["msg"],'请求成功' )
        # self.assertEqual(result["result"]["phone"],"15130078689")
        self.log.info("===end====")









if __name__ == "__main__":
    unittest.main()


