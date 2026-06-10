import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """
    Takes as parameters a 2D array, prints its shape, and
    returns a truncated version of the array based on the provided start
    and end arguments.
    """
    if not isinstance(family, list):
        raise Exception("family must be\
            a 2D array with lists of ints with the same lenght")
    if not isinstance(start, int) or not isinstance(end, int):
        raise Exception("start and end must be int values")
    for elem in family:
        if len(family[0]) != len(elem):
            raise Exception("all the list must have the same size")
    try:
        array = np.array(family)
        print(f"My shape is : {array.shape}")
        sliced_array = array[start:end]
        print(f"My new shape is : {sliced_array.shape}")
        return sliced_array.tolist()
    except Exception:
        raise Exception("all the values must be int/float values")
