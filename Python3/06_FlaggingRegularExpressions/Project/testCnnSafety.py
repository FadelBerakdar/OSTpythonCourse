#!/usr/bin/env python

# By: Fadel Berakdar
# Date: 13 Nov 2015

import unittest
from cnn_safety2 import ccn_safetyII


text = """
Have you ever noticed, in television and movies, that phone numbers and credit
cards are obviously fake numbers like 555-123-4567 or 5555-5555-5555-5555?
It is because a number that appears to be real, such as 1234-5678-1234-5678,
triggers the attention of privacy and security experts.
"""
output = """
Have you ever noticed, in television and movies, that phone numbers and credit
cards are obviously fake numbers like 555-123-4567 or CCN REMOVED FOR YOUR SAFETY?
It is because a number that appears to be real, such as CCN REMOVED FOR YOUR SAFETY,
triggers the attention of privacy and security experts.
"""


class TestCnnSafety(unittest.TestCase):
    def test_cnn_safety(self):
        self.assertEqual(output, ccn_safetyII(text))

    def test_not_none(self):
        self.assertIsNotNone(ccn_safetyII(text))

if __name__ == "__main__":
    unittest.main()
