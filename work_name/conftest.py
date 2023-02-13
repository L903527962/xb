import pytest
from pythoncode.calc import Calculator

@pytest.fixture()
def login(request):
    print("开始计算")
    calc = Calculator()
    print(request.param)
    yield
    print("结束计算")
