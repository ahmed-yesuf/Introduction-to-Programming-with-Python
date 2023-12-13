import sys


def main():
    # Check if only one command-line argument is provided
    if len(sys.argv) < 2:
        print("Too few command-line arguments")
        sys.exit(1)
    elif len(sys.argv) > 2:
        print("Too many command-line arguments")
        sys.exit(2)

    # Check if the provided argument is python file
    file_name = sys.argv[1]
    extension = file_name.strip().split(".")[1]
    if extension != "py":
        print("Not a Python file")
        sys.exit(3)

    # print LOC
    print(line_of_code(file_name))


def line_of_code(file_name):
    # Initialize count
    count = 0
    # Open file
    with open(file_name) as file:
        for line in file:
            line = line.strip()
            if line.startswith("#") or line == "":
                continue
            else:
                count += 1

        return count

if __name__=="__main__":
    main()
