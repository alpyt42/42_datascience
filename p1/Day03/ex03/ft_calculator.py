class Calculator:
    """
    A calculator class for performing arithmetic operations 
    between a vector and a scalar.
    """

    def __init__(self, vector):
        """ Initialize the Calculator with a vector. """
        self.vector = vector

    def __add__(self, scalar):
        """ Add a scalar to each element of the vector. """
        result = [x + scalar for x in self.vector]
        print(result)
        return result

    def __mul__(self, scalar):
        """ Multiply each element of the vector by a scalar. """
        result = [x * scalar for x in self.vector]
        print(result)
        return result

    def __sub__(self, scalar):
        """ Subtract a scalar from each element of the vector. """
        result = [x - scalar for x in self.vector]
        print(result)
        return result

    def __truediv__(self, scalar):
        """ Divide each element of the vector by a scalar. """
        if scalar == 0:
            raise ZeroDivisionError("Division by zero is not allowed.")
        result = [x / scalar for x in self.vector]
        print(result)
        return result

# Test script
def main():
    try:
        v1 = Calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
        v1 + 5
        print("---")
        v2 = Calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
        v2 * 5
        print("---")
        v3 = Calculator([10.0, 15.0, 20.0])
        v3 - 5
        v3 / 0
    except Exception as e:
        print(e)

if __name__ == '__main__':
    main()
