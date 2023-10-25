#!/usr/bin/python3
"""Class Rectangle"""
from models.base import Base


class Rectangle(Base):
    """Represents rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initialie rectangle class
        Args:
            width (int): width of rectangle
            height (int): height of rectangle
            x (int): x coordinate of rectangle
            y (int): y coordinate of rectangle
            id (int): id of rectangle
        Raises:
            TypeError: if width, height, x, y, or id is not an int
            ValueError: if width, height, x, y, or id is <= 0
        """

        self.width = width
        self.height = height
        self.x = x
        self.y = y

        super().__init__(id)

        # Getter methods for width, height, x, and y
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
            self.__width = value

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
            self.__height = value

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
            self.__x = value

        @property
        def y(self):
            """
            Getter method for y
            """
            return self.__y

        # Setter methods for width, height, x, and y

        @y.setter
        def y(self, value):
            """
            Setter method for y
            """
            self.__y = value
