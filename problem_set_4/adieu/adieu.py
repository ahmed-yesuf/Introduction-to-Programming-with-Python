import inflect

def main():
    # Accept list of names
    names = accept_names()

    # join words
    print(join_names(names))


def accept_names():
    # Define a list for containing names
    names = []

    # Prompt for imput
    while True:
        try:
            names.append(input("Input: "))
        except EOFError:
            break

    return names

def join_names(names):
    p = inflect.engine()

    # check if only one name is provided
    if len(names) == 1:
        return f'Adieu, adieu, to {names[0]}'
    else:
        # Change list into tuple
        n = tuple(names)
        return f'Adieu, adieu, to {p.join(n)}'


if __name__ == "__main__":
    main()
    
