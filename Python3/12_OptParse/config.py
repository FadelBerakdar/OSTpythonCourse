#!/usr/bin/env python

# config.py: get configuration form addressBook.cfg
# By: Fadel Berakdar
# Date: 26 Jan 2016
import configparser


"""
Python's configparser library provides an easily used API for interacting with
one of the popular formats used to save configurations, the INI file format.
Frequently associated with Microsoft Windows, INI is in fact also used by other
platforms such as Linux and Mac OS X.
"""


# create a config parser object
config = configparser.RawConfigParser()

# open and read the addressBook.cfg file into the config parser
config.read('addressBook.cfg')

# loop through the sections
for section in config.sections():
    print(section)
    # get all the options for the current section
    for option in config.options(section):
        # print the option and its value indented for clarity
        text = ' %s = %s' % (option, config.get(section, option))
        print(text)