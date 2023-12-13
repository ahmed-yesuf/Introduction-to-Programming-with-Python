# replace ':)' by '🙂' and ':(' by '🙁'
def main():
    s = input("String: ")
    print(convert(s))

def convert(s):
    # replace ':)' by '🙂' and ':(' by '🙁'
    return s.replace(':)', '🙂').replace(':(', '🙁')


if __name__ == "__main__":
    main()
