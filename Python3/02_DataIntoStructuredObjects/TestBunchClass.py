#!/usr/bin/env python

# O'Reilly school of technology
# Python3
# Simple Bunch Class
# By: Fadel Berakdar

import unittest
from BunchClass import Bunch


class TestBunch(unittest.TestCase):

    def setUp(self):
        self.b = Bunch(name="Python3", language="Python 3.4.1")
        self.data = self.b.pretty()

    def test_attributes(self):
        # there is no need for this test anymore, thanks to hasattr, setattr :)
        self.assertEqual("Python3", self.b.name)
        self.assertEqual("Python 3.4.1", self.b.language)

    def test_pretty(self):
        self.assertTrue("name: Python3" in self.data)


if __name__ == "__main__":
    unittest.main()


