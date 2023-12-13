import pytest
from jar import Jar


def test_init():
    jar = Jar(12)
    assert jar.capacity == 12
    assert jar.size == 0

    with pytest.raises(ValueError):
        jar = Jar(-10)


def test_str():
    jar = Jar(12)
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(5)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar(12)
    jar.deposit(3)
    assert jar.size == 3
    jar.deposit(9)
    assert jar.size == 12

    with pytest.raises(ValueError):
        jar.deposit(1)


def test_withdraw():
    jar = Jar(12)
    jar.deposit(5)
    jar.withdraw(3)
    assert jar.size == 2

    with pytest.raises(ValueError):
        jar.withdraw(3)

if __name__ == "__main__":
    test_init()
    test_str()
    test_deposit()
    test_withdraw()
