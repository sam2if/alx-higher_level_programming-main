#!/usr/bin/python3

""" 4-inherits_from module for checking instance """


def inherits_from(obj, a_class):
    """ method for checking if an obj
        is instance of a class

        Args:
            obj: instance of a class
            a_class: class the instance is created from

        Return:
            True: if obj is instance of a class
            False: Otherwise

    """
    if isinstance(obj, a_class) and type(obj) is not a_class:
        return True
    else:
        return False
