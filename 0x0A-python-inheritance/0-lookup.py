#!/usr/bin/python3

""" 0-lookup module for returning available attributes an methods """


def lookup(obj):
    """ function for returning avialble attribute
        and methods


        Args:
            obj: instance of a class

        Return:
            Avilable attributes and methods
    """
    return (dir(obj))
