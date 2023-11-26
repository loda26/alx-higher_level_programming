#!/usr/bin/python3
"""Module of print_square method"""

def print_square(size):
    """
    Method to print the square

    Args:
        size: input L and W
    
    Raise:
        TypeError: if size is not int
        ValueError: if size in < 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be an integer")
    
    print((("#" * size + "\n") * size), end="")

    if __name__ == "__main__":
        import doctest
        doctest.testfile("tests/4-print_square.txt")
