def main():
    # Accept str from user
    twttr(input("Input: "))

def twttr(string):
    # Define a list containing vowels
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    # Omit any vowels
    for s in string:
        if s not in vowels:
            print(s, sep='', end='')
    print()


if __name__ == "__main__":
    main()
