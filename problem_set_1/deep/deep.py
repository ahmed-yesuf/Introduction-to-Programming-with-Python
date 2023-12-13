# deep tought
def main():
    ans = input("What is the Answer to the Great Question of Life, the Universe and Everything? ")
    if tought(ans):
        print("Yes")
    else:
        print("No")

def tought(ans):
    match ans.strip().lower():
        case "42" | "forty-two" | "forty two":
            return True
        case _:
            return False


if __name__ == "__main__":
    main()

