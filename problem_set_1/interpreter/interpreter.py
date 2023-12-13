# math expression interpreter
def main():
    expr = input("Expression: ")
    print(interprete(expr))

def interprete(expr):
    x, y, z = expr.split(" ")
    x, z = int(x), int(z)

    if y == "+":
        return f"{x + z:.1f}"
    elif y == "-":
        return f"{x - z:.1f}"
    elif y == "/":
        return f"{x / z:.1f}"
    elif y == "*":
        return f"{x * z:.1f}"
    else:
        return "unsupported operator"


if __name__ == "__main__":
    main()
