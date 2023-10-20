#!/usr/bin/python3
"""
This module has an empty class named BaseGeometry
"""


class BaseGeometry:
    """
    Class description for Base Geometry
    """
    def area(self):
        """
        Public instance method that raise an Exception
        """
        raise Exception('area() is not implemented')
    
    def integer_validator(self, name, value):
        """
        Public instance that validates value
        """
        if type(value) is not int:
            raise TypeError("{} must be aninteger")

        elif value <=0:
            raise ValueError("{}must be greater than 0")
        
        else:
            self.name= name
            self.value= value
