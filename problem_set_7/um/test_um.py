from um import count


def test_count_no_um():
    assert count("yummy") == 0
    assert count("umbrella") == 0

def test_count_one_um():
    assert count("um") == 1
    assert count("um?") == 1
    assert count("Um, thanks for the album") == 1
    assert count("uM...") == 1

def test_count_multiple_um():
    assert count("Um, thanks, um...") == 2


if __name__=="__main__":
    test_count_no_um()
    test_count_one_um()
    test_count_multiple_um()

