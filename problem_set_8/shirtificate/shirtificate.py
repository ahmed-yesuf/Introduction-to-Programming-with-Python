import sys
from fpdf import FPDF


class Shirtificate(FPDF):
    def header(self):
        """
        Add header text at the top of the page
        """
        # Setting font: helvetica bold 15
        self.set_font("helvetica", "B", 45)
        # Moving cursor to the right:
        self.cell(80)
        # Printing title:
        self.cell(30, 10, "CS50 Shirtificate", border=0, align="C")
        # Performing a line break:
        self.ln(1)

    def create_shirtificate(self, name):
        """
        create shirtificate by printing the name of the student on the shirt.
        """
        if not name:
            print("Name not provided")
            sys.exit(1)

        # Set document propperty
        self.set_auto_page_break(auto=True, margin=15)

        # Add shirt image
        self.image("shirtificate.png", x=40, y=40, w=130)

        # Add name on the shirt
        self.set_font("helvetica", "B", 18)
        self.set_text_color(255, 255, 255)  # White text color
        # Performing a line break:
        self.ln(80)
        self.cell(80)
        self.cell(30, 10, f"{name} took CS50", border=0, align="C")


def main():
    # Prompt for name
    name = input("What's your name? ")

    shirtificate = Shirtificate(orientation='portrait', unit='mm', format='A4')
    shirtificate.add_page()
    shirtificate.create_shirtificate(name)

    # Save the PDF file
    shirtificate.output("shirtificate.pdf")


if __name__ == "__main__":
    main()

