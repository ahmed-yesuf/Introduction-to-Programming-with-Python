from plates import is_valid


def test_statrs_with_2_letter():
    # Must start with at least two letters
    assert is_valid("12CDAV") == False
    assert is_valid("ABCD12") == True

def test_min_2_char():
    # There should be a minimum of two characters
    assert is_valid("A23456") == False
    assert is_valid("AB1234") == True

def test_max_character():
    # Maximum number of characters allowed is 6
    assert is_valid("ABCDAE12") == False
    assert is_valid("ABC12") == True

def test_number_at_end():
    # Numbers should come at the end of the plate not in between
    assert is_valid("AAA222") == True
    assert is_valid("AAA22A") == False

def test_first_num():
    # The first number can't be 0
    assert is_valid("AAA022") == False
    assert is_valid("AAA202") == True

def test_no_special_char_and_punctuation():
    # There shouldn't be a space, special char, punctuation...
    assert is_valid("AA!222") == False
    assert is_valid("AA.222") == False
    assert is_valid("AA$222") == False
    assert is_valid("AA 222") == False

