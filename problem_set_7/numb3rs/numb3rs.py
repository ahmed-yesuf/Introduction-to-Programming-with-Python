import re

def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    """
    ip: ip address
    Returns True for valied ipv4 adress else False
    """
    if octates := re.search(r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$", ip):
        for octate in octates.groups():
            try:
                if not (0<=int(octate)<=255):
                    return False
            except ValueError:
                return False
        return True
    return False

if __name__ == "__main__":
    main()

