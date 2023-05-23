#!/usr/bin/python3
""" Square Module """
from . import rectangle


class Square(rectangle.Rectangle):
    """ Square class that inherits from Rectangle class """

    def __init__(self, size, x=0, y=0, id=None):
        """ Square Inits.

        Args:
            size: size of square
            x: x coordinate of sqaure
            y: y coordinate of sqaure
            id: integer value
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ String representation of the object """
        return "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """ getter method for width of sqaure

            Return:
                width of a square
        """
        return self.width

    @property
    def size(self):
        """ getter method for height of sqaure

            Return:
                height of a square
        """
        return self.width

    @size.setter
    def size(self, value):
        """ setter method for size of square

            Args:
                size: size of the square
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ method for updating attributes

            Args:
                args: non key word argument
                kwargs: key word argument
        """
        attrlist = ['id', 'size', 'x', 'y']

        if args is not None and len(args) != 0:
            for i in range(len(args)):
                setattr(self, attrlist[i], args[i])
        else:
            for key, val in kwargs.items():
                if key in attrlist:
                    setattr(self, key, val)

    def to_dictionary(self):
        """ method for dictionary representation of a Square

            Return:
                dictionary representation of a Square
        """
        my_dict = {}
        my_dict.update({"id": self.id, "x": self.x})
        my_dict.update({"size": self.width, "y": self.y})
        return my_dict
