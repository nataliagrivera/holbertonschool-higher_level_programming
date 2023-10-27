#!/usr/bin/python3
""" Rectangle class """
from models.base import Base


class Rectangle(Base):
    """Represents a rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initilizes the rectangle.

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
        #  self.if = id
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Returns the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        """Sets the width of the rectangle"""
        self.__width = value

    @property
    def height(self):
        """Returns the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        """Sets the height of the rectangle"""
        self.__height = value

    @property
    def x(self):
        """Returns the x coordinate of the rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        """Sets the x coordinate of the rectangle"""
        self.__x = value

    @property
    def y(self):
        """Returns the y coordinate of the rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        """Sets the y coordinate of the rectangle"""
        self.__y = value

    def area(self):
        """Returns the area of the rectangle"""
        return self.__width * self.__height

    def display(self):
        """Prints the rectangle using the # character"""
        for i in range(self.__y):
            print()
        for i in range(self.__height):
            print(' ' * self.__x, end='')
            print('#' * self.__width)

    def update(self, *args, **kwargs):
        """Updates the attributes of the rectangle"""
        if args:
            attrs = ['id', 'width', 'height', 'x', 'y']
            for i in range(len(args)):
                setattr(self, attrs[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def __str__(self):
        """Returns a string representation of the rectangle"""
        return '[Rectangle] ({}) {}/{} - {}/{}'.format(self.id, self.__x,
                                                       self.__y, self.__width,
                                                       self.__height)

    def to_dictionary(self):
        """Returns the dictionary representation of the rectangle"""
        return {'id': self.id, 'width': self.__width, 'height': self.__height,
                'x': self.__x, 'y': self.__y}
