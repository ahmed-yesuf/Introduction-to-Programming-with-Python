import os
from PIL import Image, ImageOps
import sys

def main():
    # list of valid extensions
    valid_ext = [".jpg", ".jpeg", ".png", ".JPG", ".JPEG", ".PNG"]

    # Check if exactly two CL arguments are provided
    if len(sys.argv) < 3:
        print("Too few command-line arguments")
        sys.exit(1)
    elif len(sys.argv) > 3:
        print("Too many command-line arguments")
        sys.exit(2)
    else:
        input = sys.argv[1]
        output = sys.argv[2]

    # Check if the specified input exists
    if not os.path.exists(input):
        print("Input does not exist")
        sys.exit(3)

    # check if input and output have different extensions
    input_ext = os.path.splitext(input)[1]
    output_ext = os.path.splitext(output)[1]

    # check if input extension is valid
    if not input_ext in valid_ext:
        print("Invalid input")
        sys.exit(4)

    # check if output extension is valid
    if not output_ext in valid_ext:
        print("Invalid output")
        sys.exit(4)

    # check if input and output have the same extension
    if input_ext != output_ext:
        print("Input and output have different extensions")
        sys.exit(5)

    # overlay picture on the t-short to see if it fits
    overlay_images(input, output)

def overlay_images(input, output):
     # Load input image
     img = Image.open(input)
     # Load shirt image
     shirt = Image.open("shirt.png")

     # Resize input image to fit the shirt
     shirt_width, shirt_height = shirt.size
     img = ImageOps.fit(img, (shirt_width, shirt_height))

     # Overlay the two images
     result_img = img.copy()
     result_img.paste(shirt, shirt)

     # Save the resulting image
     result_img.save(output)


if __name__=="__main__":
    main()

