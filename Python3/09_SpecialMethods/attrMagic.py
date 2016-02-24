#!/usr/bin/env python

"""
Demonstrate magic method for attribute access

In object- oriented languages , a mixin class  is  a class  that contains  a
certain behavior to  be inherited by subclas s es  to  add specific behaviors.
A class  can inherit some or all of its behaviors  from  one or more mixins.
Ending the nam e with "Mixin" is  no t required; it's  s im ply a flag so  that
your behavior- focused classes  are clearly delineated.
"""


class AttrMixin:
    """Displays a message when an instance's."""
    def __setattr__(self, key, value):
        print("ATTR: setting attribute {0!r} to {1!r}".format(key, value))
        self.__dict__[key] = value

    def __getattr__(self, item):
        print("ATTR: getting attribute {0!r}".format(item))
        self.__setattr__(item, "No value")
        return "No value"

    def __delattr__(self, item):
        print("ATTR: Deleting Key {0!r}".format(item))
        object.__delattr__(self, item)



class Person(AttrMixin):
    """
    Represents a person
    """
    def __init__(self, name):
        self.name = name


steve = Person("Steve Holden")
steve.age
steve.age = 20
print(steve.__dict__)

print(20 * "=")

del steve.age
print(steve.__dict__)