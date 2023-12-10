#!/usr/bin/python3
"""Defines a square class."""
from models.rectangle import Rectangle


class Square(Rectangle):
	"""Represent a square."""

	def __init__(self, size, x=0, y=0, id=None):
		"""Initialize a new Square"""
		super().__init__(size, size, x, y, id)
	
	@property
	def size(self):
		"""Get/set the size of the Square."""
		return self.width

	@size.setter
	def size(self, value):
		self.width = value
		self.height = value
	
	def __update(self, id=None, size=None, x=None, y=None):
		"""internal method to handle the update"""
		if id is not None:
			self.id = id
		if size is not None:
			self.size = size
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
	
	def to_dictionary(self):
		"""Return the dictionary representation of the Rectangle."""
		return {"id": self.id, "x": self.x, "size": self.size, "y": self.y}

	def __str__(self):
		"""Return the info of a Square."""
		return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)
