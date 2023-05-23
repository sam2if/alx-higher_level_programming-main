#!/usr/bin/python3

""" Module 6-load_from_json_file to create object from a JSON file """


def load_from_json_file(filename):
    """ a function that creates an
        Object from a “JSON file”

        Args:
            filename: json file name
    """
    import json

    with open(filename) as a_file:
        return json.load(a_file)
