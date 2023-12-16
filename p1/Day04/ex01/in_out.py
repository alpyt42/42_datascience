def square(x: int | float) -> int | float:
    return x * x

def pow(x: int | float) -> int | float:
    return x ** x

def outer(x: int | float, function) -> object:
    def inner() -> float:
        nonlocal x  # To refer to the 'x' defined in the outer function
        x = function(x)
        return x

    return inner

if __name__ == "__main__":
    my_counter = outer(3, square)
    print(my_counter())
    print(my_counter())
    print(my_counter())
    print("---")
    another_counter = outer(1.5, pow)
    print(another_counter())
    print(another_counter())
    print(another_counter())
