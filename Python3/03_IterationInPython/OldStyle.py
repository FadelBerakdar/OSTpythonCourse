#!/usr/bin/env python

# Old Style Iteration:
# if an object doesnt have __iter__() method but has __getitem__()

# Approximate equivalent of:

# for val in o:
# # [loop body] intern = 0
# while True:
#   try:
#       val = o[intern]
#   except IndexError:
#       break
# [loop body]
#   intern += 1

class Fls(object):
    """
    Simple demonstration of the "old iteration protocol
    """
    def __init__(self, val, times):
        self.val = val
        self.count = times

    """
    def __getitem__(self, item):
        if item >= self.count:
            raise IndexError("Object has no item")
        return self.val

    """
thing = Fls("*", 5)
for c in thing:
    print(c)

