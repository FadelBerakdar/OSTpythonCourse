#!/usr/bin/env python

# zipcheck.py: validation function for US zip codes
# By: Fadel Berakdar
# Date: 1 Oct 2015

import unittest
from zipCheck import zip_errors


class TestZipCode(unittest.TestCase):
    """
    US Zip code problem:
    * The zip code must be a string of length five or ten characters
    * The first five must be numeric
    * if the length of the string is ten, the sixth character must be a
         minus sign and the last four must be numeric.

    """
    def test_zip_errors(self):
        """ Tests ensuring that errors in data cause validation failures."""
        self.assertIsNotNone(zip_errors("1234"), "accepting 4 digits")
        self.assertIsNotNone(zip_errors("12345-678"), "accepting 9 digits")
        self.assertIsNotNone(zip_errors("1234r"), "accepting length 5 alphapatic")
        self.assertIsNotNone(zip_errors("12345-678e"), "accepting length 10 alpha")
        self.assertIsNotNone(zip_errors("12345/1234"), "accepting other than -")

    def test_zip_successes(self):
        """"Test ensuring that valid data passes."""
        self.assertIsNone(zip_errors("12345"), "Not accepting 5 digits")
        self.assertIsNone(zip_errors("12345-1234"), "Not accepting 10 digits")

if __name__ == "__main__":
    unittest.main()

"""
Notice that separation between the tests of good zips and the tests of bad zips
made it somewhat easier to observe that the test coverage was improving.
The fact that the second test always succeeded simply shows that the code was
developing along the right lines. Had it failed at any time, you would have seen
 that the validator was failing to approve valid data, which wo uld have been
 valuable feedback.
So , that gives yo u a brief introduction to data validation in Python.
Ideally yo u s ho uld never us e data that has no t been through some validation
process. Failure to validate inputs is the source of many well-known security
issues, including "buffer overflow" attacks and "SQL Injection" attacks.
All data that flows into a system should be validated. Once it is stored by a
program that has validated it the data can generally be considered trustworthy,
but any new inputs from outside (users, even remote servers in certain cases)
should be treated with suspicion. Get in the habit of validating your data, and
make sure that you use tested validation routines so you can have a reasonable
degree of confidence that they are go ing to validate as expected.
"""
