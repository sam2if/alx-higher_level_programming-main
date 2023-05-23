#!/usr/bin/python3

""" Module 5-save_to_json_file to save Object to a file """


def save_to_json_file(my_obj, filename):
    """ A function that writes an Object to a text
        file, using a JSON representation

        Args:
            my_obj: python object
            filename: json filename
    """
    import json

    with open(filename, 'w') as a_file:
        json.dump(my_obj, a_file)
