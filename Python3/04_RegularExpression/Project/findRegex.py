#!/usr/bin/env python

# By: Fadel Berakdar
# Date: 12 Nov 2015


"""
create a program named find_regex.py that takes the following text and finds the
start and end positions of the phrase, "Regular Expressions."


Your project should meet the following conditions:
•	Your code must return 231 as the start and 250 as the end.
•	You must include a separate test_find_regex.py program that confirms that
    your code functions as instructed.

"""


import re


def regex_finder(pattern, string):
    try:
        return re.search(pattern, string).span()
    except AttributeError:
        return None

file = open("text.txt", "r").read()

print(regex_finder("Stephen", file))

