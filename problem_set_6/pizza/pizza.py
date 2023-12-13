import csv
import os
import sys
from tabulate import tabulate

def main():
    # check if on;y one file is provided
    if len(sys.argv) < 2:
        print("Too few command-line arguments")
        sys.exit(1)
    elif len(sys.argv) > 2:
        print("Too many command-line arguments")
        sys.exit(2)

    # Check if the provided file is csv
    file_path = sys.argv[1]
    extension = os.path.splitext(file_path)[1]
    if extension != ".csv":
        print("Not a CSV file")
        sys.exit(3)

    # Check if the file exists
    if not os.path.exists(file_path):
        print("File does not exist")
        sys.exit(4)

    # Print table
    print_table(file_path)


def print_table(file_path):
    # initialize table
    table = []
    with open(file_path) as file:
        reader = csv.reader(file)
        for row in reader:
            table.append(row)
    # Print table
    print(tabulate(table, headers="firstrow", tablefmt="grid"))

if __name__=="__main__":
    main()

