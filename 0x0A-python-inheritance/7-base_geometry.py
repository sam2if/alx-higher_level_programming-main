#!/usr/bin/python3

""" 7-base_geometry module """


class BaseGeometry:
    """ class for calculating area """

    def area(self):
        """ a method that raises exception """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """ a method that validate values """
        if type(value) is not int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
