#!/usr/bin/env python

#       Testing the functionality of the adder.py
#             test_adder.py

# By: Fadel Berakdar
# Date: 2 Oct 2015


import unittest
from adder import supper_adder


class TestSupperAdder(unittest.TestCase):

    def test_failure(self):
        """
        testing type errors.
        """
        self.assertRaises(TypeError,supper_adder(1,"a"))

    def test_success(self):
        """
        Testing valid data.
        """
        self.assertEqual(supper_adder(1,1), 2, "1 + 1 = 2 !!!")


if __name__ == "__main__":
    unittest.main()
