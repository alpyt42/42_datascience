class calculator:
    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """Calculate the dot product of two vectors."""
        result = sum([x * y for x, y in zip(V1, V2)])
        print("Dot Product is:", result)

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """Add two vectors."""
        result = [float(x) + float(y) for x, y in zip(V1, V2)]
        print("Add Vector is:", result)

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """Subtract two vectors."""
        result = [float(x) - float(y) for x, y in zip(V1, V2)]
        print("Sous Vector is:", result)

def main():
    try:
        a = [5, 10, 2]
        b = [1.3, 4, 3]
        calculator.dotproduct(a,b)
        calculator.add_vec(a,b)
        calculator.sous_vec(a,b)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
