#!/usr/bin/python3

""" Module 1-write_file that writes into a file """


def write_file(filename="", text=""):
    """ function that writes a string to a text file
        and returns the number of characters added

        Args:
            filename: name of the file
            text: text to be wrote to the file
        Return:
            number of characters added
    """

    with open(filename, mode='w+', encoding='utf-8') as a_file:
        a_file.write(text)
        return len(text)
