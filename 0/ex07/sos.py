import sys


NESTED_MORSE = {" ": "/", "A": ".-", "B": "-...", "C": "-.-.",
                "D": "-..", "E": ".", "F": "..-.", "G": "--.",
                "H": "....", "I": "..", "J": ".---", "K": "-.-",
                "L": ".-..", "M": "--", "N": "-.", "O": "---",
                "P": ".--.", "Q": "--.-", "R": ".-.", "S": "...",
                "T": "-", "U": "..-", "V": "...-", "W": ".--",
                "X": "-..-", "Y": "-.--", "Z": "--..", "1": ".----",
                "2": "..---", "3": "...--", "4": "....-", "5": ".....",
                "6": "-....", "7": "--...", "8": "---..", "9": "----.",
                "0": "-----"
                }


def main():
    """ Convert your message in Morse code """
    try:
        assert len(sys.argv) == 2, "the arguments are bad"
        morse = ''
        for c in sys.argv[1]:
            if c.isalnum() or c.isspace():
                morse += NESTED_MORSE[c.upper()] + " "
            else:
                raise AssertionError("the arguments are bad")
        print(morse)
    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main()
