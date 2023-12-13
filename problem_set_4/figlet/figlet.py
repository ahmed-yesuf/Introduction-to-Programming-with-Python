from random import choice
import sys
from pyfiglet import Figlet

if not (len(sys.argv) == 1 or len(sys.argv) == 3):
    sys.exit('Invalid usage')

# Get available fonts
figlet = Figlet()
available_fonts = figlet.getFonts()

if len(sys.argv) == 3:
    # Check if 1st argument is correct
    if not (sys.argv[1] == '-f' or sys.argv[1] == '--font'):
        sys.exit("Invalid usage")

    # Check if second argument is correct
    # Get available fonts
    if sys.argv[2] not in available_fonts:
        sys.exit("Invalid usage")


def main():
    # Accept string of text
    text = input('Input: ')

    # Select font
    if len(sys.argv) == 3:
        f = sys.argv[2]
    else:
        f = choice(available_fonts)
    # Display text in desired form
    print(desired_font(text, f))

def desired_font(text, f):
    figlet.setFont(font=f)
    return figlet.renderText(text)


if __name__ == "__main__":
    main()

