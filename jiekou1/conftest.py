import pytest


@pytest.fixture(scope="function")
def login(request):
    print("登录")
    print(request.param)
    yield ["homework","password"]
    print("不登录")
