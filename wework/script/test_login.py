import unittest
from wework.api.wework_login import LoginApi


class Test_Login(unittest.TestCase):
    def setUp(self) -> None:
        # 获取返回值与token
        self.login_Api = LoginApi().login()

    def test_login(self):
        response = self.login_Api
        access_token = self.login_Api.json().get('access_token')

        self.assertIn('200',str(response))

