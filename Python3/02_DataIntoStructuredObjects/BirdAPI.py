#!/usr/bin/env python

# O'Reilly school of technology
# Python3
# API for software birds carrying objects.
# BirdAPI.py
# By: Fadel Berakdar

# The first step in designing an API is to figure out:
#       what data it should handle?
#       what behaviors it should have?

from BunchClass import Bunch


class Bird(Bunch):
    # subclass the Bunch class, allowing us to build on existing code
    """
    API for software birds carrying objects.
    """
    def pretty(self):
        """
        Replacement pretty() method inherited from the class Bunch()
        """
        return "Such a pretty bird!!\n"

    def add(self, name, value):
        """
        Add an object for the Bird to carry in its basket.
        Name is what you call the object.
        Value is the actual object being placed in the basket.
        """
        if hasattr(self, name):
            raise KeyError("'{}' object cant be placed in basket".format(name))
        else:
            setattr(self, name, value)

    def remove(self, name):
        """
        Remove an object from the basket.
        Name is the string of the object to be removed.
        """
        if name in self.__dict__:
            delattr(self, name)
        else:
            raise KeyError("'%s' object not found in the basket" % self.name)

    def calculate(self):
        """
        Calculate the speed of the bird.
            Algorithm: 100 - (5*number of objects in the basket).
            Result cannot be less than zero.
        """
        return max(100 - len(self.__dict__)*10, 0)

    def basket(self):
        """
        Print the list of objects in the basket in an attractive format.
        """
        return (20 * "=") + "\n   Basket objects\n" + (20 * "=") + "\n" + \
                            self.pretty() + (20 * "=")

if __name__ == "__main__":
    swallow = Bird(fruit="Coconut", juice="Carrot")
    swallow.add("cars", "3")
    print(swallow.basket())
    print(swallow.calculate())
    swallow.remove("juice")
    print(swallow.basket())
    print(swallow.calculate())
