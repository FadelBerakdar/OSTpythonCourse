#!/usr/bin/env python

# Old Style Iteration:
# if an object has __iter__()

# Approximate equivalent of: # for val in o:
# # [loop body]
# it = o.__iter__()
# while True:
#   try:
#       val = it.__next__()
#   except StopIteration:
#       break
# [loop body]







