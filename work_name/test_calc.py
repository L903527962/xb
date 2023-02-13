import pytest
from pythoncode.calc import Calculator


@pytest.mark.parametrize("login", [(1, 1, 2)], indirect=True)
def test_add(login):
    # cal = Calculator()
    # assert result == self.cal.add(a, b)
    print("moni")
