#!/usr/bin/env python

# O'Reilly school of technology
# Python3
# API for software birds carrying objects.
# BirdAPI.py
# By: Fadel Berakdar


class Bunch(object):
    """
    take incoming arguments and turn them to an instance attributes
    """
    def __init__(self, *args, **kwargs):
        # self.__dict__.update(kwargs) in this way, we cant insure that instance
        # attributes don't mask class attributes
        for key, value in kwargs.items():
            if hasattr(self, key):
                raise AttributeError("API Conflict: '%s' is a part of the '%s' "
                                     "API." % (key, self.__class__.__name__))
            else:
                # means, add only the attributes which their names"key" are not
                # in class.__dict__
                setattr(self, key, value)

    def pretty(self):
        text = ""
        for key, value in self.__dict__.items():
            text += "%s: %s\n" % (key, value)
        return text

class Myclass(object):
    pass

old_class = Myclass()

setattr(old_class, "name", "John") # to add new instance's attribute
print(hasattr(old_class, "name"))  # to check whether an instance has a specific attribute
print(getattr(old_class, "name"))  # to get the value of a specific attribute


new_class = Myclass()
print(hasattr(new_class, "name")) # to check whether the attribute "name" is class of instance attribute!



#
# newClass = Bunch(name="John", email="John@gmail.com")
# print(newClass.pretty())
#
# newClass.pretty = int
# print(newClass.pretty())
