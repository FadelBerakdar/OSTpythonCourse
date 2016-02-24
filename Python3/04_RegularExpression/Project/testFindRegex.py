#!/usr/bin/env python

# By: Fadel Berakdar
# Date: 12 Nov 2015


from findRegex import regex_finder
import unittest


class TestRegexFinder(unittest.TestCase):
    """
    Testing the regex_finder function
    """
    def setUp(self):
        file = open("text.txt", "r")
        self.data = file.read()
        file.close()

    def test_pass(self):
        """
        testing the function in which the its able to find the string
        """
        expected = (231, 250)
        observed = regex_finder(r"\bRegular\s\bExpression.", self.data)
        self.assertEqual(expected, observed)

    def test_none(self):
        """
        testing the function in case of failure to find the matching string
        """
        observed = regex_finder(r"\bRegularity.", self.data)
        self.assertIsNone(observed)


if __name__ == "__main__":
    unittest.main()
