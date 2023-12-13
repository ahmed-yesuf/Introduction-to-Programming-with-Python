# greet with non hello to get reward
def main():
    greet = input("Greeting? ")
    reward(greet)

def reward(greet):
    g = greet.strip().lower()
    if g.startswith("hello"):
        print("$0")
    elif g.startswith("h"):
        print("$20")
    else:
        print("$100")


if __name__ == "__main__":
    main()

