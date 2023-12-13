import sys
import inflect
from datetime import datetime, date


def main():
    # Accept bithday in YYYY-MM-DD format
    age_in_min = age_in_minutes(input("Bithdate in (YYYY-MM-DD format): "))
    print(formated_age_in_min(age_in_min))


def age_in_minutes(birthdate):
    # Validate date format
    try:
        datetime_birth = datetime.strptime(birthdate, "%Y-%m-%d")
        birthdate = datetime_birth.date()
    except ValueError:
        print("Invalid date")
        sys.exit(-1)

    # get current date
    today = date.today()
    # Validate birthdate
    if birthdate > today:
        print("Invalid date")
        sys.exit(-1)

    return round((today - birthdate).total_seconds()/60)


def formated_age_in_min(age_in_min):
    p = inflect.engine()
    return p.number_to_words(age_in_min, andword="").capitalize() + " " + "minutes"


if __name__ == "__main__":
    main()
