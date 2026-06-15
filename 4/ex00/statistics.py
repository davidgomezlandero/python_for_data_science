from typing import Any


def ft_statistics(*args: Any, **kwargs: Any) -> None:
    """ Calculate mean, median, quartile(25, 75), variance \
and standard deviation for args(float/int) """
    if not all(isinstance(x, (float, int)) for x in args):
        print("ERROR")
        return

    for operation in kwargs.values():
        if len(args) == 0:
            print("ERROR")
            continue

        if operation == "mean":
            print(f"mean : {sum(args) / len(args)}")
        elif operation == "median":
            sort_list = sorted(args)
            n = len(sort_list)
            if n % 2 == 1:
                pos = int(len(args) // 2)
                print(f"median : {sort_list[pos]}")
            else:
                print(f"median : \
{(sort_list[n // 2 -1] + sort_list[n // 2]) / 2}")
        elif operation == "quartile":
            pos_25 = int(len(args) // 4)
            pos_75 = int(len(args) * (3 / 4))
            sort_list = sorted(args)
            print(f"quartile : [{float(sort_list[pos_25])}, \
{float(sort_list[pos_75])}]")
        elif operation == "std":
            m = sum(args) / len(args)
            print(f"std : \
{(sum((x - m) ** 2 for x in args) / len(args)) ** 0.5}")
        elif operation == "var":
            m = sum(args) / len(args)
            print(f"var : {sum((x - m) ** 2 for x in args) / len(args)}")
