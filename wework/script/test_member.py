import unittest

from parameterized import parameterized

from wework import utils, app
from wework.data import dat
from wework.api import wework_Member_Api
from wework.api.wework_login import LoginApi


class TestMember(unittest.TestCase):
    def setUp(self) -> None:
        self.member_api = wework_Member_Api.MemberApi()
        self.access_token = LoginApi().login().json().get('access_token')
        # self.member_id = LoginApi().login().json().get('access_token')
        # self.create_data = utils.datajson('../data/create_member.json')

    @parameterized.expand(utils.datajson(app.BASE_DIR + '/data/create_member.json'))
    def test_create_mem(self, a):
        requet_body = a
        # print(requet_body)
        app.EMP_ID = requet_body.get('userid')
        create_mem = self.member_api.create_member(requet_body)
        print(create_mem.json())

    def test_delete_mem(self):
        print(app.EMP_ID)
        create_mem = self.member_api.delete_member(app.EMP_ID)
        print(create_mem.json())
