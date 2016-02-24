#!/usr/bin/env python

# By: Fadel Berakdar
# Date: 12 Nov 2015


import re
#import unittest


"""
create a program named ccn_safety.py with a function that substitutes X for all
but the last four digits of any credit card numbers in a string, returning the
updated string as its result. Use the following text as a sample:

Text to use in ccn_safety.py:


Your project should meet the following conditions:
    For our purposes, it only needs to convert numbers of the form
    XXXX-XXXX-XXXX-XXXX.
"""


text = """
Have you ever noticed, in television and movies, that phone numbers and credit
cards are obviously fake numbers like 555-123-4567 or 5555-5555-5555-5555? It is
because a number that appears to be real, such as 1234-5678-1234-5678, triggers
the attention of privacy and security experts."""

output = """
Have you ever noticed, in television and movies, that phone numbers and credit
cards are obviously fake numbers like 555-123-4567 or XXXX-XXXX-XXXX-5555? It is
because a number that appears to be real, such as XXXX-XXXX-XXXX-5678, triggers
the attention of privacy and security experts."""


def ccn_safety(string):
    #pattern = r"\d{4}-\d{4}-\d{4}"
    pattern = r"(\d{4}-){3}(?P\d{4})"
    #return re.sub(pattern, "XXXX-XXXX-XXXX-" + "\g", string)
    return re.sub(r"(\d{4}-){3}(\d{4})", "XXXX-XXXX-XXXX-"+"\g", string)



print(ccn_safety("XXXX-XXXX-XXXX-5555"))
"""


class TestCnnSafety(unittest.TestCase):
    def test_cnn_safety(self):
        self.assertEqual(output, ccn_safety(text))

if __name__ == "__main__":
    unittest.main()
"""