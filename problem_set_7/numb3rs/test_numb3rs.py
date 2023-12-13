from numb3rs import validate


def test_valid_ip_address():
    assert validate("127.0.0.1") == True
    assert validate("192.168.0.1") == True


def test_invalid_ip_address():
    assert validate("512.512.512.512") == False
    assert validate("1.2.3.1000") == False
    assert validate("192.168.0.256") == False
    assert validate("10.0.0.") == False
    assert validate("172.16.0") == False
    assert validate("-192.168.0.1") == False


def test_special_cases():
    assert validate("0.0.0.0") == True
    assert validate("255.255.255.255") == True
    assert validate("") == False


if __name__ == "__main__":
    test_valid_ip_address()
    test_invalid_ip_address()
    test_special_cases()

