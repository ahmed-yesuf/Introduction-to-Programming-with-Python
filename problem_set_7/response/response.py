from validator_collection import checkers


def main():
    """
    Checks if an email adress is valid or not
    """
    email = input("What's your email? ").strip()

    if checkers.is_email(email):
        print("Valid")
    else:
        print("Invalid")


if __name__=="__main__":
    main()

