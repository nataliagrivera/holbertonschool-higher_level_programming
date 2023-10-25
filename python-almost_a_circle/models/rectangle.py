#!/usr/bin/python3
"""Class Rectangle"""
from models.base import Base


class Rectangle(Base):
    """Represents rectangle class"""


    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initilizes the rectangle.
        Args:
        width (int): width of the rectangle
        height (int): height of the rectangle
        x (int): x coordinate of the rectangle
        y (int): y coordinate of the rectangle
        id (int): id of the rectangle
        Raises:
        TypeError: If either of width or height is not an integer
        ValueError: If either of width or height is <= 0
        TypeError: If either of x or y is not an integer
        ValueError: If either of x or y is < 0
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

        @property
        def width(self):
            """
            Getter method for width
            """
            return self.__width

        @width.setter
        def width(self, value):
            """
            Setter method for width
            """
            self.width = value

        @property
        def height(self):
            """
            Getter method for height
            """
            return self.__height

        @height.setter
        def height(self, value):
            """
            Setter method for height
            """
            self.height = value

        @property
        def x(self):
            """
            Getter method for x
            """
            return self.__x

        @x.setter
        def x(self, value):
            """
            Setter method for x
            """
            self.x = value

        @property
        def y(self):
            """
            Getter method for y
            """
            return self.__y

        @y.setter
        def y(self, value):
            """
            Setter method for y
            """
            self.y = value
