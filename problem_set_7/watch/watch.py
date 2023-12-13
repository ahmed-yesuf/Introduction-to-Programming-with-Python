import re

def main():
    print(parse(input("HTML: ")))


def parse(s):
    """
    This function extracts and returns embedded url from s.
    """
    pattern = r'src="(https?://(?:www.)?youtube\.com/embed/.+?)"'
    if match := re.search(pattern, s):
        return re.sub(r"^https?://(www.)?youtube\.com/embed", "https://youtu.be", match.group(1))
    return None


if __name__ == "__main__":
    main()