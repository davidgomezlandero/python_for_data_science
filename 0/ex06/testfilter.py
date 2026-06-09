from ft_filter import ft_filter

def is_even(value):
    return True if value % 2 == 0 else False

def main():
    print("--Original filter doc--\n")
    print(filter.__doc__)
    print("\n--Ft_filter doc--\n")
    print(ft_filter.__doc__)
    result = ft_filter(None, ["True", None, False, "Hola", 0])
    result2 = ft_filter(is_even, [1,2,3,4])
    print(result)
    print(result2)


if __name__ == "__main__":
    main()