import random

# Possible levels
levels = [1, 2, 3]

def main():
    level = get_level()

    # Generate 10 X + Y with level digits
    X = []
    Y = []
    for i in range(10):
        X.append(generate_integer(level))
        Y.append(generate_integer(level))

    # initialize count and score variables
    count = 0
    score = 0
    for i in range(len(X)):
        # Display problem
        print(f"{X[i]} + {Y[i]} = ", end='')

        # Allow 3 trial
        while count < 3:
            try:
                response = int(input())
            except ValueError:
                print("EEE")
                # Increment count
                count += 1

                # Display for prompt
                print(f"{X[i]} + {Y[i]} = ", end='')
                continue

            if response == X[i] + Y[i]:
                # increment score
                score += 1

                # reset count and break
                count = 0
                break

            else:
                print("EEE")
                count += 1
                print(f"{X[i]} + {Y[i]} = ", end='')

        if count == 3:
            # Reset count
            count = 0
            # Display result
            print(f"{X[i] + Y[i]}")


    print(f"Score: {score}")


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            assert level in levels
        except ValueError:
            continue
        except AssertionError:
            continue
        else:
            break
    return level


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)


if __name__ == "__main__":
    main()