"""
File: project.py
Description: This Python script implements an expense tracker application.
Author: Ahmed Yesuf Nurye
Warsaw, Poland
Date: 2023-07-15
"""

from pyfiglet import Figlet
import csv
from datetime import datetime
from colorama import Fore, init, Style
from tabulate import tabulate
from typing import List
import sys

init(autoreset=True) # reset color to default

class Expense:
    def __init__(self, category: str, description: str, amount: float, timestamp=datetime.now()):
        self.amount = amount
        self.category = category
        self.description = description
        self.timestamp = timestamp


class ExpenseTracker:
    def __init__(self, filename: str):
        self.expenses: List[Expense] = []
        self.filename = filename
        self.load_expenses()

    def accept_expense(self) -> None:
        """
        Add expense to the expense tracker

        :return: None
        """
        while True:
            try:
                amount = float(input("Amount> "))
                break
            except ValueError:
                print(Fore.RED + "\nPlease specify amount in numerical form\n")
                continue
        while True:
            category = input("Category> ")
            if category == "":
                print(Fore.RED + "\nEmpty category not accepted\n")
                continue
            break
        while True:
            description = input("Description> ")
            if description == "":
                print(Fore.RED + "\nEmpty description not accepted\n")
                continue
            break
        self.add_expense(category, description, amount)

    def add_expense(self, category: str, description: str, amount: float) -> None:
        """
        Add expense to the expense table

        :param amount: expense amount
        :param category: expense category
        :param description: expense description
        :type amount: float
        :type category: str
        :type description: str
        :return: None
        """
        expense = Expense(category, description, amount)
        self.expenses.append(expense)
        self.save_expenses()
        print(Fore.GREEN + "\nExpense added successfully!\n")

    def save_expenses(self) -> None:
        """
        Save the expenses in a csv file

        :return: None
        """
        fieldnames = ["Category", "Description", "Amount", "Timestamp"]
        with open(self.filename, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for expense in self.expenses:
                writer.writerow({
                    "Category": expense.category,
                    "Description": expense.description,
                    "Amount": expense.amount,
                    "Timestamp": expense.timestamp
                })

    def load_expenses(self) -> None:
        """
        Load expenses from the file

        :return: None
        """
        self.expenses = []
        try:
            with open(self.filename, "r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    category = row["Category"]
                    description = row["Description"]
                    amount = float(row["Amount"])
                    timestamp = datetime.strptime(row["Timestamp"], "%Y-%m-%d %H:%M:%S.%f")
                    expense = Expense(category, description, amount, timestamp)
                    self.expenses.append(expense)
        except FileNotFoundError:
            print(Fore.GREEN + "\nStarting with an empty expense tracker.\n")


def get_expense_table(tracker: ExpenseTracker) -> str:
        """
        Generate an expense table with ASCII style

        :param tracker: ExpenseTracker obj
        :type tracker: ExpenseTracker
        :return: ASCII art expense table
        """
        if not len(tracker.expenses):
            return Fore.LIGHTYELLOW_EX + "\nNo expense record found\n"

        headers = ["Category", "Description", "Amount"]
        rows = [[expense.category, expense.description, expense.amount] for expense in tracker.expenses]
        total = get_total_expense(tracker)
        rows.append(["Total", "", total])

        return tabulate(rows, headers=headers, tablefmt="fancy_grid")

def get_total_expense(tracker: ExpenseTracker) -> float:
        """
        Get the total expense amount from the start

        :param tracker: ExpenseTracker obj
        :type tracker: ExpenseTracker
        :return: total expense amount
        """
        return sum(expense.amount for expense in tracker.expenses)

def print_total_expense_table(tracker: ExpenseTracker) -> None:
    """
    Print the expense table

    :param tracker: ExpenseTracker obj
    :type tracker: ExpenseTracker
    :return: None
    """
    print(get_expense_table(tracker))

def calculate_average_expense(tracker: ExpenseTracker) -> float:
    """
    Calculate the average expense amount.

    :param tracker: ExpenseTracker obj
    :type tracker: ExpenseTracker
    :return: Average expense amount
    """
    if num_expenses := len(tracker.expenses):
        return get_total_expense(tracker) / num_expenses
    else:
        return 0.0

def print_average_expense(tracker: ExpenseTracker) -> None:
    """
    Prints the average expense of all time

    :param tracker: ExpenseTracker obj
    :type tracker: ExpenseTracker
    :return: None
    """
    print(f"\nAverage expense amount: ${calculate_average_expense(tracker):.2f}\n")


def get_expense_by_date(tracker: ExpenseTracker, start: datetime, end: datetime) -> str:
        """
        Get expenses for a specified time period

        :param tracker: ExpenseTracker obj
        :param start: beginning of the time period for which expense is to be calculated
        :param end: end of the time period for which expense is to be calculated
        :type tracker: ExpenseTracker
        :type start: datetime
        :type end: datetime
        :return: list of expenses for the specified time period if any or None
        """
        time_period_expenses = [expense for expense in tracker.expenses if start <= expense.timestamp <= end]
        if len(time_period_expenses):
            headers = ["Category", "Description", "Amount"]
            rows = [[expense.category, expense.description, expense.amount] for expense in time_period_expenses]
            total = sum(expense.amount for expense in time_period_expenses)
            rows.append(["Total", "", total])

            return tabulate(rows, headers=headers, tablefmt="fancy_grid")
        return Fore.LIGHTYELLOW_EX + f"\nNo expense record in period [{start} - {end}]\n"

def accept_time_period() -> dict:
    """
    Accept start and end of a time period from the user
    In addition it converts the dates from str to datetime.datetime

    :return: dict key start and end corresponding the start and end of the time period
    """
    while True:
        try:
            start = datetime.strptime(input("Enter start date (YYYY-MM-DD)> "), "%Y-%m-%d")
            end = datetime.strptime(input("Enter end date (YYYY-MM-DD)> "), "%Y-%m-%d")
        except ValueError:
            print(Fore.RED + "\nPlease enter valid dates in the required format\n")
            continue
        else:
            if start >= end:
                print(Fore.RED + "\nStart date cannot be greater than or equal to the end date\n")
                continue
        break
    return {"start": start, "end": end}

def print_expense_by_date(tracker: ExpenseTracker) -> None:
        """
        Print the expense table of a given time period

        :param tracker: ExpenseTracker obj
        :type tracker: ExpenseTracker
        :return: None
        """
        date = accept_time_period()
        start, end = date["start"], date["end"]
        print(get_expense_by_date(tracker, start, end))


def get_expenses_by_month(tracker: ExpenseTracker, month: int) -> str:
    """
    Get expenses for a specific month.

    :param tracker: ExpenseTracker obj
    :param month: Month to filter expenses
    :type tracker: ExpenseTracker
    :type month: int
    :return: List of Expense objects for the specified month
    """
    expenses_by_month = [expense for expense in tracker.expenses if expense.timestamp.month == month]

    if len(expenses_by_month):
        headers = ["Category", "Description", "Amount"]
        rows = [[expense.category, expense.description, expense.amount] for expense in expenses_by_month]
        total = sum(expense.amount for expense in expenses_by_month)
        rows.append(["Total", "", total])
        return tabulate(rows, headers=headers, tablefmt="fancy_grid")
    return Fore.LIGHTYELLOW_EX + f"\nNo expense record in month, {month}\n"

def accept_month() -> int:
    """
    Accept month from user to be used to get expense by month

    :return: int representing a specific month
    """
    while True:
        try:
            month = int(input("Enter month (MM)(1-12)> "))
        except ValueError:
            print(Fore.RED + "\nEnter numeric value for month\n")
        else:
            if not month in range(1, 13):
                continue
        break
    return month

def print_expense_by_month(tracker: ExpenseTracker) -> None:
    """
    Print expense table for given month

    :param tracker: ExpenseTracker obj
    :type tracker: ExpenseTracker
    :return: None
    """
    month = accept_month()
    print(get_expenses_by_month(tracker, month))


def get_expense_by_category(tracker: ExpenseTracker, category: str) -> str:
        """
        Get the expenses of a specific category

        :param tracker: ExpenseTracker obj
        :param category: category for which the expense is to be calculated
        :type tracker: ExpenseTracker
        :type category: str
        :return: list of expenses for the specified category if any or None
        """
        category_expenses = [expense for expense in tracker.expenses if expense.category.lower() == category.lower()]
        if len(category_expenses):
            headers = ["Category", "Description", "Amount"]
            rows = [[expense.category, expense.description, expense.amount] for expense in category_expenses]
            total = sum(expense.amount for expense in category_expenses)
            rows.append(["Total", "", total])

            return tabulate(rows, headers=headers, tablefmt="fancy_grid")
        return Fore.LIGHTYELLOW_EX + f"\nNo expense record in category, {category}\n"

def print_expense_by_category(tracker: ExpenseTracker) -> None:
        """
        Print the expense table of the given category

        :param tracker: ExpenseTracker obj
        :type tracker: ExpenseTracker
        :return: None
        """
        while True:
            category = input("Category> ")
            if category == "":
                print(Fore.RED + "\nEmpty category not accepted\n")
                continue
            break
        print(get_expense_by_category(tracker, category))


def get_expenses_by_keyword(tracker: ExpenseTracker, keyword: str) -> str:
    """
    Filter expenses based on the description containing a specific keyword.

    :param tracker: ExpenseTracker obj
    :param keyword: Keyword to filter expenses by description
    :type tracker: ExpenseTracker
    :type keyword: str
    :return: List of filtered Expense objects
    """
    filtered_expenses = [expense for expense in tracker.expenses if keyword.lower() in expense.description.lower()]

    if len(filtered_expenses):
        headers = ["Category", "Description", "Amount"]
        rows = [[expense.category, expense.description, expense.amount] for expense in filtered_expenses]
        total = sum(expense.amount for expense in filtered_expenses)
        rows.append(["Total", "", total])
        return tabulate(rows, headers=headers, tablefmt="fancy_grid")
    return Fore.LIGHTYELLOW_EX + f"\nNo expense record with keyword, {keyword}\n"

def print_expense_by_keyword(tracker: ExpenseTracker) -> None:
    """
    Prints expense table with containing given keyword in the description

    :param tracker: ExpenseTracker obj
    :type tracker: ExpenseTracker
    :return: None
    """
    while True:
        keyword = input("Enter keyword to filter expenses by description: ")
        if keyword == "":
            print(Fore.RED + "\nEmpty keyword not accepted\n")
            continue
        break
    print(get_expenses_by_keyword(tracker, keyword))


def delete_expense(tracker, category: str, description: str) -> None:
        """
        Delete expenses based on category and description

        :param category: expense category
        :param description: expense description
        :type category: str
        :type description: str
        :return: None
        """
        num_of_expenses_before = len(tracker.expenses)
        tracker.expenses = [expense for expense in tracker.expenses
                         if expense.category.lower() != category.lower() or expense.description.lower() != description.lower()]
        if len(tracker.expenses) < num_of_expenses_before:
            tracker.save_expenses()
            print(Fore.GREEN + "\nExpense deleted successfully!\n")
            return
        print(Fore.LIGHTYELLOW_EX + "\nNo record found with given category and description\n")


def update_expense(tracker, category: str, description: str, amount: float) -> None:
    """
    Update the amount of an expense based on category and description

    :param category: expense category
    :param description: expense description
    :param amount: expense amount
    :type category: str
    :type description: str
    :type amount: float
    :return: None
    """
    for expense in tracker.expenses:
       if expense.category.lower() == category.lower() and expense.description.lower() == description.lower():
            expense.amount = amount
            tracker.save_expenses()
            print(Fore.GREEN + "\nExpense updated successfully!\n")
            return
    print(Fore.LIGHTYELLOW_EX + "\nExpense not found for the given category and description.\n")


def accept_user_input(num: int) -> tuple:
    """
    Accept num number of inputs from the user

    :param num: number of inputs to accept from the user
    :type num: int
    :return: tuple
    """
    while True:
            category = input("Category> ")
            if category == "":
                print(Fore.RED + "\nEmpty category not accepted\n")
                continue
            break

    while True:
        description = input("Description> ")
        if description == "":
            print(Fore.RED + "\nEmpty description not accepted\n")
            continue
        break

    if num == 3:
        while True:
            try:
                amount = float(input("Amount> "))
                break
            except ValueError:
                print(Fore.RED + "\nPlease specify amount in numerical form\n")
                continue
        return category, description, amount
    elif num == 2:
        return category, description


def print_menu() -> None:
    print("###############################################################")
    print("##                                                           ##")
    print("##   Menu:                                                   ##")
    print("##        1. Add Expense                                     ##")
    print("##        2. View Total Expenses                             ##")
    print("##        3. View Expenses by Category                       ##")
    print("##        4. View Expenses by Time Period                    ##")
    print("##        5. View Expenses by Month                          ##")
    print("##        6. View Average Expense                            ##")
    print("##        7. Filter Expenses by Keyword                      ##")
    print("##        8. Update Expense                                  ##")
    print("##        9. Delete Expense                                  ##")
    print("##        0. Exit                                            ##")
    print("##                                                           ##")
    print("###############################################################")

def menu() -> None:
    filename = "expenses.csv"
    tracker = ExpenseTracker(filename)
    while True:
        print_menu()
        choice = input("Enter your choice (0-9): ")

        if choice == "1":
            tracker.accept_expense()
        elif choice == "2":
            print_total_expense_table(tracker)
        elif choice == "3":
            print_expense_by_category(tracker)
        elif choice == "4":
            print_expense_by_date(tracker)
        elif choice == "5":
            print_expense_by_month(tracker)
        elif choice == "6":
            print_average_expense(tracker)
        elif choice == "7":
            print_expense_by_keyword(tracker)
        elif choice == "8":
            update_expense(tracker, *accept_user_input(3))
        elif choice == "9":
            delete_expense(tracker, *accept_user_input(2))
        elif choice == "0":
            sys.exit(Fore.LIGHTRED_EX + "Exiting...")
        else:
            print("Invalid choice. Please try again.")

def logo() -> None:
    """
    Display Expense Tracker Logo
    """
    figlet = Figlet()
    figlet.setFont(font="larry3d")
    print(Fore.BLUE + figlet.renderText("EXPENSE TRACKER"))
    input(Fore.LIGHTGREEN_EX + "\nPress ENTER to continue...\n" + Style.RESET_ALL)

def main():
    logo()
    menu()

if __name__ == "__main__":
    main()

