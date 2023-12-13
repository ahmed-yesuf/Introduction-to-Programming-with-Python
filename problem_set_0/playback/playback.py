# replace ' ' with '...'
def main():
    s = input("String: ")
    print(replace(s))

def replace(s):
    # replace ' ' with '...'
    return s.replace(' ', '...')


if __name__ == "__main__":
    main()
