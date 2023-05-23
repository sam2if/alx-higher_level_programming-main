#!/usr/bin/python3

""" Module 10-student that defines student """


class Student:
    """ Student class that defines student """

    def __init__(self, first_name, last_name, age):
        """Inits Student.

        Args:
            first_name: first_name of a student
            last_name: last_name of a student
            age: age of a student

        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ function that retrieves a dictionary representation
            of a Student instance

            Args:
                attrs: specific atributes to be retrived

            Return:
                attributes in attrs

        """
        if type(attrs) is list and all(type(attr) is str for attr in attrs):
            return {key: self.__dict__[key] for key in self.__dict__
                    if key in attrs}
        else:
            return self.__dict__
