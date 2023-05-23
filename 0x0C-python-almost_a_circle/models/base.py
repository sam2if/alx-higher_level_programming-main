#!/usr/bin/python3
""" Module base other moudlues inherit from """
import json
import csv
import os


class Base:
    """ Class Base other classes inherit from """

    __nb_objects = 0

    def __init__(self, id=None):
        """ Base Inits.

            Args:
                id: integer value
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ method for getting json representation
            of a the parameter list_dictionaries

            Args:
                list_dictionaries: List dictionaries

            Return:
                Json String representation
        """
        l_dict = []

        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            for list_dictionarie in list_dictionaries:
                l_dict.append(list_dictionarie)
            return json.dumps(l_dict)

    @classmethod
    def save_to_file(cls, list_objs):
        """ method that writes json string representation
            of list_objs to a file

            Args:
                cls: current class
                list_objs: json string representation
        """
        filename = cls.__name__ + ".json"

        if list_objs is not None:
            new_list_obj = []

            for list_obj in list_objs:
                if isinstance(list_obj, cls):
                    new_list_obj.append(list_obj.to_dictionary())

            json_dict = json.loads(Base.to_json_string(new_list_obj))
            with open(filename, "w") as f:
                json.dump(json_dict, f)

        else:
            empty_list = []
            with open(filename, "w") as f:
                json.dump(empty_list, f)

    @staticmethod
    def from_json_string(json_string):
        """ method for that returns the list of the
            JSON string representation json_string

            Args:
                json_string: json string input

            Return:
                returns the list of the JSON string representation

        """
        if json_string is None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ a class method that returns
            an instance with all attributes already set

            Args:
                dictionary: key word argument

            Return:
                returns an instance with all attributes already set
        """
        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 1)
        elif cls.__name__ == 'Square':
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ class method that return list of instances

            Return:
                list of instances
        """

        filename = cls.__name__ + ".json"
        list_dicts = []
        final = []

        try:
            with open(filename, 'r') as f:
                s = f.read()
                list_dicts = cls.from_json_string(s)
                for d in list_dicts:
                    final.append(cls.create(**d))
                return final
        except:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializes list_objs in CSV format
        and saves it to a file.
        Args:
            - list_objs: list of instances
        """

        if (type(list_objs) != list and
           list_objs is not None or
           not all(isinstance(x, cls) for x in list_objs)):
            raise TypeError("list_objs must be a list of instances")

        filename = cls.__name__ + ".csv"
        with open(filename, 'w') as f:
            if list_objs is not None:
                list_objs = [x.to_dictionary() for x in list_objs]
                if cls.__name__ == 'Rectangle':
                    fields = ['id', 'width', 'height', 'x', 'y']
                elif cls.__name__ == 'Square':
                    fields = ['id', 'size', 'x', 'y']
                writer = csv.DictWriter(f, fieldnames=fields)
                writer.writeheader()
                writer.writerows(list_objs)

    @classmethod
    def load_from_file_csv(cls):
        """Deserializes CSV format from a file.
        Returns: list of instances
        """

        filename = cls.__name__ + ".csv"
        final = []
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                reader = csv.reader(f, delimiter=',')
                if cls.__name__ == 'Rectangle':
                    fields = ['id', 'width', 'height', 'x', 'y']
                elif cls.__name__ == 'Square':
                    fields = ['id', 'size', 'x', 'y']
                for x, row in enumerate(reader):
                    if x > 0:
                        i = cls(1, 1)
                        for j, e in enumerate(row):
                            if e:
                                setattr(i, fields[j], int(e))
                        final.append(i)
        return final
