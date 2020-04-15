import requests
base = 'http://172.16.20.152:7040/api/ec/'
loginUrl = base+"login"
hearders = {

            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:68.0) Gecko/20100101 Firefox/68.0",
            "Accept": "*/*",
            "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
            "Accept-Encoding": "gzip, deflate",
            "Content-Type": "application/json;charset=utf-8",
            "Content-Length": "63",
            "Connection": "keep-alive"

        }
body = {

            "credential": 123456,
            "phone": 15130078689,
            "type": "PASSWARD"
        }

s = requests.session()  # 保持会话
r = s.post(loginUrl, data=body, headers=hearders)
print(r.content)# 打印结果看到location='http://127.0.0.1/zentao/my/'说明登录成功了