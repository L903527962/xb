import os
from wework.api import wework_login
# 根目录
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# 请求头
HEADER = {'Content-Type':'application/json'}
# uil
BASE_URL='https://qyapi.weixin.qq.com/'

EMP_ID =None
# TOKEN = wework_login.LoginApi('../data/data.json').login().json()['access_token']
