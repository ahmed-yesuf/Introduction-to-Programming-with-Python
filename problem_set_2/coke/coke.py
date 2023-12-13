def main():
    user_interface()

def user_interface():
    # Define price and acceptable coins
    price = 50
    due = 50
    own = 0
    accepted = [25, 10, 5]

    while True:
        # Accept coin from user
        coin = int(input("Insert Coin: "))

        # Calculate Due or owed
        if coin in accepted:
            due = due - coin

        # Display info to the user
        if due > 0:
            print("Amount Due:", due)
        else:
            print("Change Owed:", abs(due))
            break


if __name__ == "__main__":
    main()
