def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # Reuirement_1: Must start with atleast 2 letters
    if not requirement_1(s):
        return False

    # Requirement_2: Maximum characters (6)
    min, max = 2, 6
    if not requirement_2(s, min, max):
        return False

    # Requirement_3: Number can't be used in the middle
    if not requirement_3(s):
        return False

    # Requirement_4: No period, space, and punctuation mark is alowed
    if not requirement_4(s):
        return False

    return True

def requirement_1(s):
    if s[0:2].isalpha():
        return True
    else:
        return False

def requirement_2(s, min, max):
    if min <= len(s) <= max:
        return True
    else:
        return False

def requirement_3(s):
    flag1 = None
    flag2 = None
    for c in s:
        if c.isnumeric() and flag1 is None:
            flag1 = True
            if c == '0':
                return False
        if flag1 and c.isalpha() and flag2 is None:
            flag2 = True
    if flag1 and flag2:
        return False
    else:
        return True

def requirement_4(s):
    acceptable = ['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
              'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
              '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for c in s:
        if c in acceptable:
            pass
        else:
            return False

    return True


if __name__ == "__main__":
    main()
