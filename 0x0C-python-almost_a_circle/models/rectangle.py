#!/usr/bin/python3
""" Module Rectangle """
from . import base


class Rectangle(base.Base):
    """ Rectangle class that inherits from base class """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Rectangle Init.

            Args:
                width: width of rectangle
                height: height of rectangle
                x,y: coordinate of rectangle
        """
        super().__init__(id)
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """ getter method for width

            Return: width of rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """ Setter method for width

            Args:
                width: width of rectangle
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ getter method for height

            Return: return height of rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """ setter method for height

            Args:
                height: height of a rectangle
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ getter method for x

            Return: x coordinate of rectnagle
        """
        return self.__x

    @x.setter
    def x(self, value):
        """ setter method for x

            Args:
                x: x coordinate of rectangle
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ getter method for y

            Return: y coordinate of rectangle
        """
        return self.__y

    @y.setter
    def y(self, value):
        """ setter method for y

            Args:
                y: y coordinate of rectangle
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ area method fo calculating area of rectangle

            Return: area of rectangle
        """
        return self.__width * self.__height

    def display(self):
        """ display method that prints '#' of rectangle
            based on height and width
        """
        for i in range(self.__y):
            print()
        for i in range(self.__height):
            print(" " * self.__x, end="")
            for j in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """ method for string representation of the object """
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height))

    def update(self, *args, **kwargs):
        """ method for updating class instance attributes

            Args:
                args: as many non key word argument as the user wants to pass
                kwargs: as many key word argumenr as the user wants to pass
        """
        attrlist = ['id', 'width', 'height', 'x', 'y']
        if args is not None and len(args) != 0:
            for i in range(len(args)):
                setattr(self, attrlist[i], args[i])
        else:
            for key, value in kwargs.items():
                if key in attrlist:
                    setattr(self, key, value)

    def to_dictionary(self):
        """ method for dictionary representation of a Rectangle

            Return:
                the dictionary representation of the class
        """
        my_dict = {}
        my_dict.update({"x": self.x, "y": self.y, "id": self.id})
        my_dict.update({"height": self.height, "width": self.width})

        return my_dict
