#!/usr/bin/python3
class Square:
    """class square 6"""

    def __init__(self, size=0, position=(0, 0)):
        """initialization method"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """getter method"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """setter method"""
        if type(value) != int:
            raise TypeError('size must be an integer')
        if value < 0:
