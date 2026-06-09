import sys


def ft_count(text):
    """Print counts of upper/lower/punct/spaces/digits in text."""
    print(f"The text contains {len(text)} characters:")

    upper = sum(1 for c in text if c.isupper())
    print(f"{upper} upper letters")

    lower = sum(1 for c in text if c.islower())
    print(f"{lower} lower letters")

    punct = sum(1 for c in text if not c.isalnum() and not c.isspace())
    print(f"{punct} punctuation marks")

    spaces = sum(1 for c in text if c.isspace())
    print(f"{spaces} spaces")

    digits = sum(1 for c in text if c.isdigit())
    print(f"{digits} digits")


def main():
    """Parse input and run the counting routine."""
    try:
        assert len(sys.argv) <= 2, "more than one argument is provided."
        if len(sys.argv) == 2:
            text = sys.argv[1]
            ft_count(text)
        else:
            text = ""
            try:
                while len(text) == 0:
                    print("What is the text to count?")
                    text = input()
            except (KeyboardInterrupt, EOFError):
                return
            ft_count(text)
    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == '__main__':
    main()
