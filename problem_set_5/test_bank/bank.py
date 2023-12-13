# greet with non hello to get reward
def main():
    greeting = input("Greeting? ")
    print(value(greeting))


def value(greeting):
    g = greeting.strip().lower()
    if g.startswith("hello"):
        return 0
    elif g.startswith("h"):
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
