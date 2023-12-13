from colorama import Fore
from datetime import date, datetime, timedelta
from project import ExpenseTracker
from project import calculate_average_expense
from project import get_expense_by_category
from project import get_expense_by_date
from project import get_expenses_by_keyword
from project import get_expenses_by_month
from project import get_total_expense
from tabulate import tabulate


def test_get_total_expenses():
    filename = "test.csv"
    tracker = ExpenseTracker(filename)

    tracker.add_expense("Category 1", "Expense 1", 10.0)
    assert get_total_expense(tracker) == 10.0

    tracker.add_expense("Category 2", "Expense 2", 15.0)
    assert get_total_expense(tracker) == 25.0

    tracker.add_expense("Category 1", "Expense 3", 20.0)
    assert get_total_expense(tracker) == 45.0


def test_get_expenses_by_category():
    filename = "test.csv"
    tracker = ExpenseTracker(filename)

    actual_expenses_category1 = get_expense_by_category(tracker, "Category 1")
    # Let's construct the expected expense table for category 1
    headers = ["Category", "Description", "Amount"]
    rows = [["Category 1", "Expense 1", 10.0],
            ["Category 1", "Expense 3", 20.0],
            ["Total", "", 30.0]]
    expected_expense_category1 = tabulate(rows, headers=headers, tablefmt="fancy_grid")
    assert actual_expenses_category1 == expected_expense_category1

    actual_expense_category2 = get_expense_by_category(tracker, "Category 2")
    # Let's construct the expected expense table for category 2
    headers = ["Category", "Description", "Amount"]
    rows = [["Category 2", "Expense 2", 15.0],
            ["Total", "", 15.0]]
    expected_expense_category2 = tabulate(rows, headers=headers, tablefmt="fancy_grid")
    assert actual_expense_category2 == expected_expense_category2


def test_get_expenses_by_date():
    filename = "test.csv"
    tracker = ExpenseTracker(filename)

    yesterday = (date.today() - timedelta(days=1)).strftime("%Y-%m-%d")
    tomorrow = (date.today() + timedelta(days=1)).strftime("%Y-%m-%d")

    # Convert date from string to type datetime
    yesterday = datetime.strptime(yesterday, "%Y-%m-%d")
    tomorrow = datetime.strptime(tomorrow, "%Y-%m-%d")

    actual_expense_of_today = get_expense_by_date(tracker, yesterday, tomorrow)
    # Let's construct expected expense
    headers = ["Category", "Description", "Amount"]
    rows = [["Category 1", "Expense 1", 10.0],
            ["Category 2", "Expense 2", 15.0],
            ["Category 1", "Expense 3", 20.0],
            ["Total", "", 45.0]]
    expected_expense_of_today = tabulate(rows, headers=headers, tablefmt="fancy_grid")
    assert actual_expense_of_today == expected_expense_of_today


def test_calculate_average_expense():
    filename = "test.csv"
    tracker = ExpenseTracker(filename)

    average_expense = calculate_average_expense(tracker)
    assert average_expense == 15.0


def test_get_expenses_by_keyword():
    """
    For testing the number of expenses with some keyword from the description
    """
    filename = "test.csv"
    tracker = ExpenseTracker(filename)

    actual_filtered_expenses1 = get_expenses_by_keyword(tracker, "expense")
    # Let's construct the expected filtered expense
    headers = ["Category", "Description", "Amount"]
    rows = [["Category 1", "Expense 1", 10.0],
            ["Category 2", "Expense 2", 15.0],
            ["Category 1", "Expense 3", 20.0],
            ["Total", "", 45.0]]
    expected_filtered_expenses1 = tabulate(rows, headers=headers, tablefmt="fancy_grid")
    assert actual_filtered_expenses1 == expected_filtered_expenses1

    actual_filtered_expenses2 = get_expenses_by_keyword(tracker, "expense 2")
    # Let's construct the expected filtered expense
    headers = ["Category", "Description", "Amount"]
    rows = [["Category 2", "Expense 2", 15.0],
            ["Total", "", 15.0]]
    expected_filtered_expenses2 = tabulate(rows, headers=headers, tablefmt="fancy_grid")
    assert actual_filtered_expenses2 == expected_filtered_expenses2

    keyword = "xyz"
    actual_filtered_expenses3 = get_expenses_by_keyword(tracker, keyword)
    expected_filtered_expenses3 = Fore.LIGHTYELLOW_EX + f"\nNo expense record with keyword, {keyword}\n"
    assert actual_filtered_expenses3 == expected_filtered_expenses3


def test_get_expenses_by_month():
    """
    For testing the number of expenses in a given month
    """
    filename = "test.csv"
    tracker = ExpenseTracker(filename)

    actual_expenses_current_month = get_expenses_by_month(tracker, datetime.now().month)
    # Let's construct the expected expense
    headers = ["Category", "Description", "Amount"]
    rows = [["Category 1", "Expense 1", 10.0],
            ["Category 2", "Expense 2", 15.0],
            ["Category 1", "Expense 3", 20.0],
            ["Total", "", 45.0]]
    expected_expenses_current_month = tabulate(rows, headers=headers, tablefmt="fancy_grid") # only the ones previously added
    assert actual_expenses_current_month == expected_expenses_current_month

    previous_month_date = (date.today() - timedelta(days=62)).strftime("%Y-%m-%d")
    previous_month_date = datetime.strptime(previous_month_date, "%Y-%m-%d") # Convert date to type datetime
    actual_expenses_previous_month = get_expenses_by_month(tracker, previous_month_date.month)
    assert  actual_expenses_previous_month == Fore.LIGHTYELLOW_EX + f"\nNo expense record in month, {previous_month_date.month}\n"


def main():
    test_get_total_expenses()
    test_get_expenses_by_category()
    test_get_expenses_by_date()
    test_calculate_average_expense()
    test_get_expenses_by_keyword()
    test_get_expenses_by_month()


if __name__ == "__main__":
    main()
