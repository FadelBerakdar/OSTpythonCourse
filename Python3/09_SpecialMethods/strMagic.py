#!/usr/bin/env python

# Demonstrate string representations using inheritance.
# By: Fadel Berakdar
# Date: 25 Nov 2015


class Person(object):
    "Represents a person"
    def __init__(self, name):
        self.name = name

class NamedPerson(Person):
    """
    Represents a person using their name
    The string returned by __st r__() is supposed to be an " informal"
    representation of the object, just to be readable nicely
    """
    def __str__(self):
        return self.name


person1 = Person("John")
print(person1)


person2 = NamedPerson("John")
print(person2)


