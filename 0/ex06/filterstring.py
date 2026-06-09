import sys
from ft_filter import ft_filter


def main():
    """The program output a list of words from sys.argv[1]\
        that have a length greater than sys.argv[2]"""
    try:
        assert len(sys.argv) == 3, "the arguments are bad"
        try:
            N = int(sys.argv[2])
        except ValueError:
            raise AssertionError("the arguments are bad")
        N = int(sys.argv[2])
        words = sys.argv[1].split()
        result = ft_filter(lambda x: len(x) > N, words)
        print(result)
    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main()
