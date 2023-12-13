def main():
    x, y = accept_input()
    p = calc_percent(x, y)
    print(display(p))

def accept_input():
    while True:
        # accept input
        fraction = input("Fraction: ")

        # find x and y
        try:
            f = fraction.split('/')
            x = int(f[0])
            y = int(f[1])
        except ValueError:
            pass
        else:
            if x > y:
                accept_input()
            else:
                return x, y

def calc_percent(x, y):
    try:
        return x/y*100
    except ZeroDivisionError:
        pass

def display(p):
    if p <= 1:
        return "E"
    elif p >= 99:
        return "F"
    else:
       return f"{round(p)}%"

if __name__ == "__main__":
    main()
