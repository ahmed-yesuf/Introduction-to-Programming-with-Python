# file extension
def main():
    file = input("File name: ")
    print(extension(file))

def extension(file):
    f = file.strip().lower()

    # get file extension
    ext = f.split(".")[-1]

    match ext:
        case "gif":
            return "image/gif"
        case "jpg" | "jpeg":
            return "image/jpeg"
        case "png":
            return "image/png"
        case "pdf":
            return "application/pdf"
        case "txt":
            return "text/plain"
        case "zip":
            return "application/zip"
        case _:
            return "application/octet-stream"


if __name__ == "__main__":
    main()

