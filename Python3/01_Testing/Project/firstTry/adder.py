#!/usr/bin/env python

#       Function returns the sum of two objects if they r integers
#                    adder.py

# By: Fadel Berakdar
# Date: 2 Oct 2015


def supper_adder(a, b):
    """ take two objects and add them together only if they are both of the
    integer type, Raise type error otherwise."""
    try:
        return a+b
    except TypeError:
        return
