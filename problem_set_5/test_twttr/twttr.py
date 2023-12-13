def main():
    # Accept str from user
    string = input("Input: ")
    print(shorten(string))

def shorten(word):
    # Define a list containing vowels
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

    # Omit any vowels
    new_word = []
    for s in word:
        if not s in vowels:
            new_word.append(s)
    return ''.join(new_word)


if __name__ == "__main__":
    main()
