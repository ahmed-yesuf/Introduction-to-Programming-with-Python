def main():
    time = input("What is the time? ")
    t = convert(time)
    if 7 <= t <= 8:
        print("breakfast time")
    elif 12 <= t <= 13:
        print("lunch time")
    elif 18 <= t <= 19:
        print("dinner time")


def convert(time):
    conv_factor = 60.0
    hr, min = time.split(":")

    return int(hr) + int(min)/conv_factor


if __name__ == "__main__":
    main()