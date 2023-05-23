#!/usr/bin/python3

""" Module 8-class_to_json that shows
    dictionary description with simple data structure
"""


def class_to_json(obj):
    """ a function that returns the dictionary description with
        simple data structure (list, dictionary, string,
        integer and boolean) for JSON serialization of an object

        Args:
            obj: instance of a class

        Return:
            dictionary description
    """

    return obj.__dict__
