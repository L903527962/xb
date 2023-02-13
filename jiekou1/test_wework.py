import json

import requests


class Test_Wework:
    def get_token(self):
        requ = requests.get("https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=ww3d4a3c0e0ae8908d"
                            "&corpsecret=wUOfbSmdoGe5-nZBSzigK-GtQ7ygYFoqYmzPpv3H_io")

        ret = requ.json()['access_token']
        # print(ret)

        return ret

    def get_create(self):
        access_token1 = self.get_token()
        user_name = range(100)
        request_body = {
            # "userid": "zhangsan{}".format(user_name),
            "userid": "zhangsan8",
            "name": "张三7",
            "mobile": "13800000008",
            "department": [1],
            "position": "产品经理"}
        print(json.dumps(request_body))
        cre = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={access_token1}"
                            , json=request_body)
        print(cre.json())

    def test_get_people_id(self):
        access_token = self.get_token()
        print(access_token)
        rep = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/user/list_id?access_token={access_token}")
        print(rep.json())
