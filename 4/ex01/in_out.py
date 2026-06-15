def square(x: int | float) -> int | float:
    """ Returns the square of an argument """
    return x * x


def pow(x: int | float) -> int | float:
    """ Returns the exponentiation of an argument by himself """
    return x ** x


def outer(x: int | float, function) -> object:
    """
    Returns a object with a function apply to the first argument.
    Each time you call the object the function is applied to the last result.
    """
    count = 0

    def inner() -> float:
        nonlocal count
        if count != 0:
            count = function(count)
        else:
            count = function(x)
        return count

    return inner
