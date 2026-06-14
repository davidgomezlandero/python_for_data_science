from typing import Any

def ft_statistics(*args: Any, **kwargs: Any) -> None:
    if not all(isinstance(x, (float, int)) for x in args):
        print("ERROR")
    if len(args) == 0:
        print("ERROR")
    
    statistics = ("mean", "median", "quartile", "std", "var")
    
    for operation in kwargs.values():
        if operation not in statistics or len(args) == 0:
            print("ERROR")
        
        if operation == "mean":
            print(f"mean : {sum(args) / len(args)}")
        
        if operation == "median":
            sort_list = sorted(args)
            pos = int(len(args) // 2)
            print(f"median : {sort_list[pos]}")
        
        if operation == "quartile":
            pos_25 = int(len(args) // 4)
            pos_75 = int(len(args) * (3 / 4))
            sort_list = sorted(args)
            print(f"quartile : [{float(sort_list[pos_25])}, {float(sort_list[pos_75])}]")
        
        if operation == "std":
            pass
        
        if operation == "var":
            pass
