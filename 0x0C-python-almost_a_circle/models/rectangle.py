#!/usr/bin/python3
"""Defines a rectangle class."""
from models.base import Base


class Rectangle(Base):
	"""Represent a rectangle."""

	def __init__(self, width, height, x=0, y=0, id=None):
		"""Initialize a new Rectangle.

		Args:
			width (int): The width of the new Rectangle.
			height (int): The height of the new Rectangle.
			x (int): The x coordinate of the new Rectangle.
			y (int): The y coordinate of the new Rectangle.
			id (int): The identity of the new Rectangle.
		Raises:
			TypeError: If either of width or height is not an int.
			ValueError: If either of width or height <= 0.
			TypeError: If either of x or y is not an int.
			ValueError: If either of x or y < 0.
		"""
		self.width = width
		self.height = height
		self.x = x
		self.y = y
		super().__init__(id)

	@property
	def width(self):
		"""Set/get width of the Rectangle."""
		return self.__width
	
	@width.setter
	def width(self, value):
		if type(value) != int:
			raise TypeError("width must be an integer")
		if value <= 0:
			raise ValueError("width must be > 0")
		self.__width = value
	
	@property
	def height(self):
		"""Set/get the height of the Rectangle."""
		return self.__height
	
	@height.setter
	def height(self, value):
		if type(value) != int:
			raise TypeError("height must be an integer")
		if value <= 0:
			raise ValueError("height must be > 0")
		self.__height = value
	
	@property
	def x(self):
		"""Set/get the x coordinate of the Rectangle."""
		return self.__x
	
	@x.setter
	def x(self, value):
		if type(value) != int:
			raise TypeError("x must be an integer")
		if value < 0:
			raise ValueError("x must be >= 0")
		self.__x = value
	
	@property
	def y(self):
		"""Set/get the y coordinate of the Rectangle."""
		return self.__y
	
	@y.setter
	def y(self, value):
		if type(value) != int:
			raise TypeError("y must be an integer")
		if value < 0:
			raise ValueError("y must be >= 0")
		self.__y = value
	
	def area(self):
		"""Return the area of the Rectangle."""
		return self.width * self.height
	
	def display(self):
		"""Print the Rectangle using the `#` character."""
		# if self.width == 0 or self.height == 0:
		# 	print("")
		# 	return
		
		# [print("") for y in range(self.y)]
		# for h in range(self.height):
		# 	[print(" ", end="") for x in range(self.x)]
		# 	[print("#", end="") for w in range(self.width)]
		# 	print("")
		s = '\n' * self.y + (' ' * self.x + '#' * self.width + '\n') * self.height
		print(s, end='')

	def __update(self, id=None, width=None, height=None, x=None, y=None):
		"""internal method to handle the update"""
		if id is not None:
			self.id = id
		if width is not None:
			self.width = width
		if height is not None:
			self.height = height
		if x is not None:
			self.x = x
		if y is not None:
			self.y = y

	def update(self, *args, **kwargs):
		"""Update the Rectangle"""
		if args:
			self.__update(*args)
		elif kwargs:
			self.__update(**kwargs)

	def __str__(self):
		"""Return the dictionary representation of a Rectangle."""
		return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,self.x, self.y,self.width, self.height)
