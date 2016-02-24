#!/usr/bin/env python

#       Function returns the sum of two objects if they r integers
#                    adder.py

# By: Fadel Berakdar
# Date: 6 Oct 2015


def supper_adder(a, b):
    """
    take two objects and add them together only if they are both of the
    integer type, Raise type error otherwise.
    """
    both_are_int = isinstance(a, int) and isinstance(b, int)
    both_are_not_bool = not(isinstance(a, bool) or isinstance(b, bool))

    if both_are_int and both_are_not_bool:
        return a+b
    else:
        raise TypeError("Only integers are accepted!!")

