#!/usr/bin/python3

""" 1-my_list module for inheriting a list """


class MyList(list):
    """ MyList drived class that inherits
        from superclass list
    """

    def print_sorted(self):
        """
        print sorted list

        """
        new_list = self[:]
        new_list.sort()
        print("{}".format(new_list))
