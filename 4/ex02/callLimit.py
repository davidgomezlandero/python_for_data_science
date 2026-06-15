from typing import Any


def callLimit(limit: int):
    """
    Create a decorator that restricts a function to a
    maximum number of calls.
    """
    count = 0

    def callLimiter(function):
        """
        Wrap a function so its calls are tracked and limited.
        """

        def limit_function(*args: Any, **kwds: Any):
            """
            Call the wrapped function if under the call limit.
            """
            nonlocal count
            if count < limit:
                count += 1
                return function(*args, **kwds)
            else:
                print(f"Error: {function} call too many times")
                return None

        return limit_function
    return callLimiter
