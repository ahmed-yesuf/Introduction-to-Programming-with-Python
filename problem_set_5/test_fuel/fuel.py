def main():
    fraction = input("Fraction: ")
    percentage = convert(fraction)
    print(gauge(percentage))


def convert(fraction):
    # find x and y form "x/y"
    f = fraction.split('/')
    try:
        x = int(f[0])
        y = int(f[1])
    except ValueError:
        raise

    if x > y and y != 0:
        raise ValueError("X can't be greater than y")

    try:
        return x/y*100
    except ZeroDivisionError:
        raise


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{round(percentage)}%"


if __name__ == "__main__":
    main()

