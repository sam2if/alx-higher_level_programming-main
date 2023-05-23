#!/usr/bin/python3

""" Module 2-append_write that appends a string at the end of a text file """


def append_write(filename="", text=""):
    """ function that writes or append a text to end of a file
        and returns the number of characters added

        Args:
            filename: file name to be appended to
            text: text to be appended

        Return:
            and returns the number of characters added
    """
    with open(filename, mode='a', encoding='utf-8') as a_file:
        a_file.write(text)
        return len(text)
