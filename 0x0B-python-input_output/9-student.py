#!/usr/bin/python3

""" Module 9-student that defines student """


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

    def to_json(self):
        """ that retrieves a dictionary representation
            of a Student instance """
        return self.__dict__
