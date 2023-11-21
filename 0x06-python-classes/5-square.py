#!/usr/bin/python3
"""Square module."""

class Square:
    """Defines a square."""

    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return self.__size ** 2

    def my_print(self):
        for i in range(self.size):
            for j in range(self.size):
                print("#", end='\n' if j is sef.size - 1 and i != j else "")
            print()
