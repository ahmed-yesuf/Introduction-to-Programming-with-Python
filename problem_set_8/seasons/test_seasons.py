import pytest
from datetime import date, timedelta
from seasons import age_in_minutes


def test_age_in_minutes():
    # Test case 1: birthdate is today
    today = date.today().strftime("%Y-%m-%d")
    assert age_in_minutes(today) == 0

    # Test case 2: birthdate is exactly one year ago
    one_year_ago = (date.today() - timedelta(days=365)).strftime("%Y-%m-%d")
    assert age_in_minutes(one_year_ago) == 525600

    # Test case 2: birthdate in the future
    next_year = (date.today() + timedelta(days=365)).strftime("%Y-%m-%d")
    with pytest.raises(SystemExit) as exc_info:
        age_in_minutes(next_year)
        assert exc_info.value.code == -1  # sys.exit()

    # Test case 3: Invalid format birthdate
    with pytest.raises(SystemExit) as exc_info:
        age_in_minutes(next_year)
        assert age_in_minutes("1965/12/5") == -1  # sys.exit()

