# convert var name from camel case to snake case
def main():
    camel_case = input("Variabele name: ")
    snake_case(camel_case)

def snake_case(c_c):
    for c in c_c:
        if c.islower():
            print(c, sep='', end='')
        else:
            print('_' + c.lower(), end='')
    print()


if __name__ == "__main__":
    main()