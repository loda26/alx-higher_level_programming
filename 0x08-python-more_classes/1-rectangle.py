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