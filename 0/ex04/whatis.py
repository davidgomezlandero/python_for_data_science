import sys

if __name__ == "__main__":
    try:
        assert len(sys.argv) <= 2, "more than one argument is provided"
        if len(sys.argv) < 2:
            sys.exit(0)

        try:
            value = int(sys.argv[1])
        except ValueError:
            raise AssertionError("argument is not an integer")

        print("I'm Even.") if value % 2 == 0 else print("I'm Odd.")
    except AssertionError as e:
        print(f"AssertionError: {e}")