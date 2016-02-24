#!/usr/bin/env python
# By: Fadel Berakdar
# date: 22 Nov 2015


class Furnishings(object):
    def __init__(self, room):
        self.room = room


class Sofa(Furnishings):
    counter = 0

    def __init__(self, room):
        super().__init__(room)
        Sofa.counter += 1


class BookShelf(Furnishings):
    counter = 0

    def __init__(self, room):
        super().__init__(room)
        BookShelf.counter += 1


class Bed(Furnishings):
    counter = 0

    def __init__(self, room):
        super().__init__(room)
        Bed.counter += 1


class Table(Furnishings):
    counter = 0

    def __init__(self, room):
        super().__init__(room)
        Table.counter += 1


def map_home(lst):
    objects_dict = {}
    for instance in lst:
        if instance.room not in objects_dict.keys():
            # I couldn't know why i cant do
            # objects_dict[instance.room] = [].append(instance)
            objects_dict[instance.room] = []
            objects_dict[instance.room].append(instance)
        else:
            objects_dict[instance.room].append(instance)
    return objects_dict


def counter(lst):
    """
    a counter function to count number of occurrences for each class
    :param lst: list of objects
    :return: None
    """
    objects_dict = {}
    for instance in lst:
        if instance.__class__.__name__ not in objects_dict.keys():
            objects_dict[instance.__class__.__name__] = 1
        else:
            objects_dict[instance.__class__.__name__] += 1
    for key, value in objects_dict.items():
        # sorry for messing up with the english grammar :P
        print("{} : {}".format(key, value))


def cute_counter(lst):
    """
    a counter function to count number of occurrences for each class which
    utilizes the class data members
    :param lst: a list of objects
    :return: None
    """
    objects_dict = {}
    for instance in lst:
        objects_dict[instance.__class__.__name__] = instance.__class__.counter

    for key, value in objects_dict.items():
        # sorry for messing up with the english grammar :P
        print("{}s : {}".format(key, value))
