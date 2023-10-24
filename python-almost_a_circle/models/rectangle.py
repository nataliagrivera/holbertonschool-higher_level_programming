#!/usr/bin/python3 
"""Class Rectangle"""


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

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
    
        # Getter methods for width, height, x, and y
    def get_width(self):
        return self.__width

    def get_height(self):
        return self.__height

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    # Setter methods for width, height, x, and y
    def set_width(self, width):
        if width > 0:
            self.__width = width
        else:
            print("Width must be greater than 0.")

    def set_height(self, height):
        if height > 0:
            self.__height = height
        else:
            print("Height must be greater than 0.")

    def set_x(self, x):
        self.__x = x

    def set_y(self, y):
        self.__y = y
