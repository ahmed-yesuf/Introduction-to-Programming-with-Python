import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    """
    s time in 12 hour formar
    Return 24 hour format
    """
    pattern = r"^(\d{1,2}(?::\d{2})? (?:AM|PM)) to (\d{1,2}(?::\d{2})? (?:AM|PM))$"
    if matches := re.search(pattern, s):
        return f"{get_12hr_format(matches.group(1))} to {get_12hr_format(matches.group(2))}"
    else:
        # Raise value error if format is invalid
        raise ValueError("Invalid format")


def get_12hr_format(hr):
    """
    hr: 12 hour format time
    Return:
           24 hour time format
    """
    time, meridiem = hr.split(" ")
    if ":" in time:
        hr, min = time.split(":")
    else:
        hr, min = time, "00"

    if invalid_time(hr, min):
        # if the time is invalied like 12:60 also raise value error
        raise ValueError("Invalid time")

    if meridiem == "AM":
        if hr != "12":
            return f"{int(hr):02d}:{min}"
        else:
            return f"00:{min}"
    else:
        if hr != "12":
            return f"{int(hr)+12:02d}:{min}"
        else:
            return f"12:{min}"

def invalid_time(hr, min):
    """
    Accepts hr and min
    Return:
           True if hr and min are in the valid range else False
    """
    try:
        if not (0<=int(hr)<=12 and 0<=int(min)<60):
            return True
        return False
    except ValueError:
        return True

if __name__ == "__main__":
    main()