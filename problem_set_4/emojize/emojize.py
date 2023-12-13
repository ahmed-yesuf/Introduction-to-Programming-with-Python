import emoji

def main():
    # Accept input tobe emojized, it may contain aditional string
    text = input("Input: ")
    # Convert to emoji
    print(convert(text))

def convert(text):
    start_idx = text.find(':')
    if start_idx != 0:
        # we have additional text separated by comma
        t = text.split(', ')
        return f'{t[0]}, {emoj(t[1])}'
    else:
       return emoj(text)

def emoj(name):
    return emoji.emojize(name, language='alias')


if __name__ == "__main__":
    main()

