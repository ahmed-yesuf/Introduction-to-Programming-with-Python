def main():
    date = accept_date()
    print(date)

def accept_date():
    m = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]

    while True:
        date = input("Date: ")
        if '/' in date:
            d = date.split('/')
            try:
                if not 1 <= int(d[0]) <= 12 or not 1 <= int(d[1]) <= 30:
                    continue
            except ValueError:
                continue
            
            try:
                return f'{int(d[2]):02}-{int(d[0]):02}-{int(d[1]):02}'
            except IndexError:
                continue

        elif ',' in date:
            d = date.split(',')
            try:
                dm = d[0].split()
            except:
                continue

            if dm[0] not in m or not 1 <= int(dm[1]) <= 30:
                continue
            try:
                return f'{int(d[1]):02}-{m.index(dm[0]) + 1:02}-{int(dm[1]):02}'
            except IndexError:
                continue


if __name__ == "__main__":
    main()
