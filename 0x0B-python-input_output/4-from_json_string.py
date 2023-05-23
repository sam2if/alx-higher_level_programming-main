#!/usr/bin/python3

""" Module 4-from_json_string to change json to object """


def from_json_string(my_str):
    """ A function that returns an object (Python data structure)
        represented by a JSON string

        Args:
            my_str: json object

        Return:
            Python equavalent representattion of json

    """
    import json

    return json.loads(my_str)
