import unittest

from wework.script.test_login import Test_Login
from wework.script.test_member import TestMember
import HTMLTestRunner_PY3
import time

time.strftime('%Y%m%d_%H%M%S')
# 创建测试套件
suite = unittest.TestSuite()
# 将测试用例添加至测试套件
suite.addTest(unittest.makeSuite(Test_Login))
suite.addTest(unittest.makeSuite(TestMember))
with open(f'./report/report.html', 'wb') as f:
    runner = HTMLTestRunner_PY3.HTMLTestRunner(f)
    runner.run(suite)
