# 企业微信token
import requests

from wework import app
from wework.data import dat


class LoginApi:
    def __init__(self):
        self.url = app.BASE_URL+'cgi-bin/gettoken?'
        self.data = dat.data('../data/data.json')
        # print(self.data)

    def login(self):
        requ = requests.get(f"{self.url }corpid={self.data.get('corpid')}"
                            f"&corpsecret={self.data.get('corpsecret')}")
        # 获取token
        # ret = requ.json()['access_token']
        #
        # return ret

        return requ


if __name__ == '__main__':
    l = LoginApi()
    print(l.login().json().get("access_token"))
    # print(l.login().json()['access_token'])
