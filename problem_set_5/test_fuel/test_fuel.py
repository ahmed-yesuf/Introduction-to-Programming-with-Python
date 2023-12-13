import pytest
from fuel import convert, gauge


def test_convert_raise_value_err():
    with pytest.raises(ValueError):
        convert("X/Y")

    with pytest.raises(ValueError):
        convert("3/2")

def test_convert_raise_zero_div_err():
    with pytest.raises(ZeroDivisionError):
        convert("2/0")

def test_convert_normal():
    assert convert("1/4") == 25
    assert convert("1/2") == 50
    assert convert("1/100") == 1

def test_gauge_empty():
    assert gauge(1) == "E"
    assert gauge(0) == "E"

def test_gauge_full():
    assert gauge(99) == "F"
    assert gauge(100) == "F"

def test_gauge_half():
    assert gauge(50) == "50%"

