#!/usr/bin/python3
"""Defines a class Rectangle"""

class Rectangle:
    """Representation of a Rectangle"""
    def __init__(self, width=0, height=0):
        """H & W"""
        self.height = height
        self.width = width
    
    @property
    def width(self):
        """getter for att W"""
        return self.__width
    
    @width.setter
    def width(self, value):
        """setter for W"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
    
    @property
    def height(self):
        """getter for att H"""
        return self.__height
    
    @height.setter
    def height(self, value):
        """setter for H"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
    
    def area(self):
        """return area of Rec"""
        return self.__width * self.__height
    
    def perimeter(self):
        """return the perim of Rec"""
        if self.__height == 0 or self.__width == 0:
            return 0
        
        return (self.__width * 2) + (self.__height * 2)
    
    def __str__(self):
        """return printed string in form of Rec"""
        rect = []
        for i in range(self.__height):
            [rect.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))
