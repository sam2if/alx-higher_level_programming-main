#!/usr/bin/python3

""" 3-is_kind_of_class.py module for checking instance """


def is_kind_of_class(obj, a_class):
    """ method for checking if an obj
        is instance of a class

        Args:
            obj: instance of a class
            a_class: class the instance is created from

        Return:
            True: if obj is instance of a class
            False: Otherwise

    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
