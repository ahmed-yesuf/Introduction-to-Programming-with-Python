# Accept grocery items
def main():
    grocery = accept_item()
    print_item(grocery)

def accept_item():
    grocery = {}
    while True:
        try:
            item = input().upper()
        except EOFError:
            print()
            break
        grocery[item] = grocery.get(item, 0) + 1

    return grocery

def print_item(grocery):
    for key in sorted(grocery.keys()):
        print(grocery[key], key)


if __name__ == "__main__":
    main()
    