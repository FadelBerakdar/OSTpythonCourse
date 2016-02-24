#!/usr/bin/env python
# By: Fadel Berakdar
# date: 28 Jan 2016

import unittest
from propertyAddress import Address, ZipCodeError, StateError
import shlex
import subprocess


class TestAdress(unittest.TestCase):
    def setUp(self):
        self.home = Address(name="Steve Holden",
                            street_address="1972 Flaying Circus",
                            city="Arlingtonn",
                            state="VAV",
                            zip_code="12345-1234")

    def test_name(self):
        self.assertEqual(self.home.name, "Steve Holden")
        self.assertRaises(AttributeError, setattr, self.home, "name",
                          "Daniel Creenfeld")

    def test_state(self):
        self.assertEqual(self.home.state, "VAV")
        self.assertRaises(StateError, setattr, self.home, "state", "Not  state")
        self.home.state = "COV"
        self.assertEqual(self.home.state, "COV")


    def test_zip_code(self):
        self.assertEqual(self.home.zip_code, "12345-1234")
        self.assertRaises(ZipCodeError, setattr, self.home, "zip_code","123456")
        self.home.zip_code = "54321-4321"
        self.assertEqual(self.home.zip_code, "54321-4321")

    # this is my try to test the program with subprocess
    def test_optparse_all_arg(self):
        command_line = './propertyAddress.py -l WARNING -n Tom -a "my street"' \
                       ' -c "San Diego" -s "CAC" -z 12345-1234'
        args = shlex.split(command_line)
        self.assertTrue(subprocess.Popen(args))

    def test_optparse_level_missing(self):
        command_line = './propertyAddress.py -n Tom -a "my street" -c ' \
                       '"San Diego" -s "CAC" -z 12345-1234'
        args = shlex.split(command_line)
        self.assertTrue(subprocess.Popen(args))


    def test_optparse_state(self):
        command_line = './propertyAddress.py -l WARNING -n Tom -a "my street"' \
                       ' -c "San Diego" -s "not state" -z 12345-1234'
        args = shlex.split(command_line)
        self.assertRaises(ValueError, subprocess.Popen, args)

    def test_optparse_zip_code(self):
        command_line = './propertyAddress.py -l WARNING -n Tom -a "my street"' \
                       ' -c "San Diego" -s "CCC" -z 12345'
        args = shlex.split(command_line)
        self.assertRaises(ValueError, subprocess.Popen, args)


if __name__ == '__main__':
    unittest.main()

