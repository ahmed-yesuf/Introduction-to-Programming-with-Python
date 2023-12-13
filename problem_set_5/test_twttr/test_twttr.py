from twttr import shorten


def test_lower():
    assert shorten("aeiou") == ""

def test_upper():
    assert shorten("AEIOU") == ""

def test_twitter():
    assert shorten("twitter") == "twttr"

def test_string():
    assert shorten("Hi There Number 2!") == "H Thr Nmbr 2!"

