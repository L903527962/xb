import pytest

@pytest.mark.parametrize(
    "login",[
        ("username","password"),
        ("username1","password1"),
    ],
    indirect=True
)
def test_cart1(login):
    print("购物车用例3")


def test_case2():
    print("case2")


def test_case3(login):
    print("case3")
