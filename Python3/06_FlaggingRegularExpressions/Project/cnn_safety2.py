#!/usr/bin/env python

# By: Fadel Berakdar
# Date: 13 Nov 2015

"""
create a program named ccn_safety2.py that duplicates the ccn_safety.py
program's functionality, but uses a compiled regular expression to replace the
credit card numbers in the paragraph with "CCN REMOVED FOR YOUR SAFETY".

Your project should meet the following conditions:
•	The program should return this text:
•	You should include a test_ccn_safety2.py program in a separate file that
    confirms that your code functions as expected.
•	You must use the re.VERBOSE flag to properly document each element of the
    pattern used to identify credit card numbers.
"""

import re


def ccn_safetyII(string):
    regex = re.compile(r"\d{4}-\d{4}-\d{4}-\d{4}", re.VERBOSE)
    return regex.sub("CCN REMOVED FOR YOUR SAFETY", string)
