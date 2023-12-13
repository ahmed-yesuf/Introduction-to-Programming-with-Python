import csv
import sys
import os


def main():
    # Check if one additional argument is provided
    if len(sys.argv) < 3:
        print("Too few command-line arguments")
        sys.exit(1)
    elif len(sys.argv) > 3:
        print("Too many command-line arguments")
        sys.exit(2)
    else:
        file_path_1 = sys.argv[1]
        file_path_2 = sys.argv[2]

    # Check if the file exist
    extension_1 = os.path.splitext(file_path_1)[1]
    extension_2 = os.path.splitext(file_path_2)[1]

    # Check if the file exist
    if not os.path.exists(file_path_1):
        print(f"Could not read {file_path_1}")
        sys.exit(3)

    # Check if both files extension is csv
    if extension_1 != ".csv":
        print(f"Could not read {file_path_1}")
        sys.exit(3)
    if extension_2 != ".csv":
        print(f"Could not write to {file_path_2}")
        sys.exit(3)

    process_file(file_path_1, file_path_2)

def process_file(file_path_1, file_path_2):
    # Read and process file
    # Initialize output_row
    output_rows = []
    with open(file_path_1) as file:
        reader = csv.DictReader(file)
        for row in reader:
            house = row["house"]
            name = row["name"]
            last, first = name.split(", ")
            output_rows.append({"first": first, "last": last, "house": house})
    # Write file with the desired format
    field_names = ["first", "last", "house"]
    with open(file_path_2, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=field_names)
        writer.writeheader()
        writer.writerows(output_rows)

if __name__=="__main__":
    main()
