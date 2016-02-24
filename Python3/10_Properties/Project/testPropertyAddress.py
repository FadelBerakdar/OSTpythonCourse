#!/usr/bin/env python
# By: Fadel Berakdar
# date: 22 Jan 2016

import unittest
from propertyAddress import *


class TestAdress(unittest.TestCase):
    def setUp(self):
        self.home = Address(name="Steve Holden",
                            street_address="1972 Flaying Circus",
                            city="Arlingtonn",
                            state="VA",
                            zip_code="12345")

    def test_name(self):
        self.assertEqual(self.home.name, "Steve Holden")
        self.assertRaises(AttributeError, setattr, self.home, "name",
                          "Daniel Creenfeld")

    def test_state(self):
        self.assertEqual(self.home.state, "VA")
        self.assertRaises(StateError, setattr, self.home, "state", "Not  state")
        self.home.state = "CO"
        self.assertEqual(self.home.state, "CO")

    def test_zip_code(self):
        self.assertEqual(self.home.zip_code, "12345")
        self.assertRaises(ZipCodeError, setattr, self.home, "zip_code","123456")
        self.home.zip_code = "54321"
        self.assertEqual(self.home.zip_code, "54321")


if __name__ == "__main__":
    unittest.main()
