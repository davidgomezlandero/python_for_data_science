def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    """ Calculates the BMI of a list of people """
    if len(height) != len(weight):
        raise Exception("different length between height and weight")
    for i in range(len(height)):
        if not isinstance(height[i], (int,
                                      float)) or isinstance(height[i], bool):
            raise Exception("all values must be int/float")
        if not isinstance(weight[i], (int,
                                      float)) or isinstance(weight[i], bool):
            raise Exception("all values must be int/float")

    return [(weight[i] / (height[i])**2) for i in range(len(height))]


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """ Returns True if the bmi is above the limit and False if not """
    if not isinstance(limit, int):
        raise Exception("limit must be an int")
    for v in bmi:
        if not isinstance(v, (int, float)):
            raise Exception("all bmi values must be int/float")
    return [c > limit for c in bmi]
