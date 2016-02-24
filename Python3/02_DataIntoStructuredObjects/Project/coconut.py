#!/usr/bin/env python

# By: Fadel Berakdar
# Date: 10 Nov 2015


class Inventory(object):
    """
    Inventory class that tracks different types of coconuts from
    around the world.
    """
    def __init__(self):
        self.coconuts_lst = []

    def add_coconut(self, coconut_object):
        """
        accepts a coconut as an argument. Other types throw an AttributeError.
        :parameter coconut_object
        """
        if isinstance(coconut_object, Coconut):
            self.coconuts_lst.append(coconut_object.__class__)

        else:
            raise AttributeError("Please enter a coconut type object")

    def total_weight(self):
        """
        A method returns the total weight in the inventory
        """
        return sum(coconut.weight for coconut in self.coconuts_lst)


class Coconut:
    pass


class SouthAsian(Coconut):
    weight = 3


class MiddleEastern(Coconut):
    weight = 2.5


class American(Coconut):
    weight = 3.5
