total = 0.0

def main():
    accept_item()

# accept order untill ctrl + d
def accept_item():
    while True:
        try:
            item = input("Item: ")
        except EOFError:
            print()
            break
        else:
            print_price(item)

def print_price(item):
    items = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
    }

    global total
    item = item.title()

    if item in items:
        total += items[item]
    else:
        pass
    print(f"Total: ${total:.2f}")


if __name__ == "__main__":
    main()
    