#!/usr/bin/env python

#
# By: Fadel Berakdar
# Date: 25 Nov 2015

"""
Demonstrate differences between __str__() and __repr__().
"""


class Neither(object):
    pass


class StrOnly(object):
    def __str__(self):
        return "STR"


class ReprOnly(object):
    def __repr__(self):
        """
        The goal of __repr__ is to be unambiguous
        the goald to produces  the object being represented. Its  prim ary use
        is  in debugging or logging, and is  bes t no t revealed to  us ers .
        The information should be as rich as  possible.
        :return: "REPR"
        """
        return "REPR"


class Both(StrOnly, ReprOnly):
    pass


class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        """
        The goal of __str__ is to be readable
        :return: string that's  nicely printable representation of an object
        """
        return self.name

    def __repr__(self):
        """
        The goal of __repr__ is to be unambiguous
        :return: a string containing a printable representation of an object
        """
        return "Person ({0.name!r}), {0.age!r}".format(self)
        # Note that it uses the !r format effector to include the formal
        # representations of the instance's name and age. Raw String



o1 = Neither()
print("o1: ", str(o1), repr(o1))

o2 = StrOnly()
print("o2: ", str(o2), repr(o2))

o3 = ReprOnly()   # the __repr__() method is used for both str() repr()
print("o3: ", str(o3), repr(o3))

o4 = Both()
print("o4", str(o4), repr(o4))

