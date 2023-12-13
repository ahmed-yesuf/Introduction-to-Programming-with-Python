import random

def main():
    # prompt for a Level
    level = get_input("Level: ")

    # Generate random int between 1 and level
    actual_val = random.randint(1, level)

    # give user response whether they are correct or not
    simulate_game(level, actual_val)

def get_input(prompt):
    # Accept user input
    while True:
        try:
            user_in = int(input(prompt))
        except ValueError:
            continue
        if user_in > 0:
            break
    return user_in

def simulate_game(level, actual_val):
    while True:
        # accept guess
        guess = get_input("Guess: ")

        if guess > actual_val:
            print("Too large!")
            continue

        elif guess < actual_val:
            print("Too small!")
            continue
        else:
            print("Just right!")
            break


if __name__ == "__main__":
    main()

