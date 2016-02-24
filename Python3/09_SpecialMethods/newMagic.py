#!/usr/bin/env python

# By: Fadel berakdar
# Date: 25 Nov 2015

# __new__ First look !

# Technically, instance creation first triggers the __new__ method, which
# creates and returns the new instance object, which is then passed into
# __init__ for initialization. Since __new__ has a built-in implementation and
# is redefined in only very limited roles, though, nearly all Python classes
# initialize by defining an __init__ method. though rare, it is sometimes also
# used to customize creation of instances of immutable types.

# __init__ initiate a new instance of a class
# __init__ returns nothing
# __init__ receives the arguments that the caller passes when calling the class.

# __new__ returns an object that will be used as return value of the
# instantiation call.
# __new__ receives a first argument that is the class to be created rather than
# the newly-created instance. which is cls but not self
# __new__( ) metho d (inherited fro m the object type) can be us ed to create
# immutable o bject ins tances

"""
Python classes with __new__ magic Method
"""


class Ustr(str):  # subclass of the class str
    "An upper case string object"
    def __new__(cls, arg):
        # The cls parameter is the actual class that was called
        arg = str(arg)
        return str.__new__(cls, arg.upper())


new_string = Ustr("hello! its me :D")
old_string = "Hello!"

print(type(new_string))
print(type(old_string))

a = Ustr("Hi")
b = str("Hi")
aSet = set(dir(a))
bSet= set(dir(b))
print(len(a), len(b))
print(aSet.difference(bSet))
print(bSet.difference(aSet))

a.size = 12
b.size = 12

