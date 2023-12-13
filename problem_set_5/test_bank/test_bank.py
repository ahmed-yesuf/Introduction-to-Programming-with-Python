from bank import value

def test_lower():
    assert value("hello") == 0
    assert value("hi") == 20
    assert value("what's up") == 100

def test_upper():
    assert value("HELLO") == 0
    assert value("HI") == 20
    assert value("WHAT'S UP") == 100

def test_mixed():
    assert value("HeLLo There") == 0
    assert value("hI") == 20
    assert value("WhAt'S uP!") == 100

