import requests

from wework import app
from wework.api.wework_login import LoginApi

"""
成员管理

"""


class MemberApi(object):
    def __init__(self):
        self.url_create = app.BASE_URL + "cgi-bin/user/create?"
        self.url_get = app.BASE_URL + "user/create"
        self.url_delete = app.BASE_URL + "cgi-bin/user/delete?"
        self.HEADER = app.HEADER
        self.access_token = LoginApi().login().json().get('access_token')

    # 创建成员
    def create_member(self, request_body):
        # print(f"{self.url_create}access_token={self.access_token}")
        return requests.post(f"{self.url_create}access_token={self.access_token}"
                             , json=request_body,
                             headers=app.HEADER)

    # 获取成员
    def get_member(self):
        pass

    # 删除成员
    def delete_member(self, userid):
        # print(f"{self.url_delete}access_token={self.access_token}&userid={userid}")
        return requests.get(f"{self.url_delete}access_token={self.access_token}&userid={userid}")


if __name__ == '__main__':
    mem = MemberApi()
    jdata = {
        "userid": "101",
        "name": "张wu",
        "mobile": "13800000095",
        "department": [1],
        "position": "产品经理"
    }
    a = mem.create_member(jdata)
    d = mem.delete_member(jdata.get("userid"))
    print(a.json())
    print(d.json())
