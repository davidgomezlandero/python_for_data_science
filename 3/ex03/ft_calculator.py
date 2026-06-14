class calculator:
    """ Calculator class for vector-scalar operations """

    def __init__(self, vector):
        """ Calculator class constructor """
        self.vector = vector

    def __add__(self, scalar) -> None:
        """ Add scalar to each element: vector + scalar """
        self.vector = [x + scalar for x in self.vector]
        print(self.vector)

    def __mul__(self, scalar) -> None:
        """ Multiply each element by scalar: vector * scalar """
        self.vector = [x * scalar for x in self.vector]
        print(self.vector)

    def __sub__(self, scalar) -> None:
        """ Subtract scalar to each element: vector - scalar """
        self.vector = [x - scalar for x in self.vector]
        print(self.vector)

    def __truediv__(self, scalar) -> None:
        """ Divide each element by scalar: vector / scalar """
        if scalar == 0:
            print("Error: Division by 0")
            return
        self.vector = [x / scalar for x in self.vector]
        print(self.vector)
