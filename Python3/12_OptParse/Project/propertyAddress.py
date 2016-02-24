#!/usr/bin/env python
# By: Fadel Berakdar
# date: 28 Jan 2016

import re
import logging
from optparse import OptionParser
import configparser


config = configparser.RawConfigParser()  # create a config parser object
config.read('propertyAddress.cfg')  # open and read the log file into the config
file = config.get('log', 'output')
formatting = config.get('log', 'format')
zip_code_pattern = r"" + config.get('validators', 'zip_code')
state_pattern = r"" + config.get('validators', 'state')


def start_logging(log_file, level, log_format):
    """
    Start logging with given filename and level.
    :param log_file: the log file name
    :param level: the level of built-in logger functions
    :param log_format: the log formatting
    :return: None
    """
    levels = {'debug': logging.DEBUG,
              'info': logging.INFO,
              'warning': logging.WARNING,
              'error': logging.ERROR,
              'critical': logging.CRITICAL}

    logging.basicConfig(filename=log_file,
                        level=levels[level],
                        format=log_format)
    logging.info('Starting up the propertyAddress program')  # log a message


def is_state(state):
    if not re.match(state_pattern, state):
        logging.error("State exception")
        raise StateError(state)


def is_zip_code(zip_code):
    if not re.match(zip_code_pattern, zip_code):
        logging.error("Zip code exception")
        raise ZipCodeError(zip_code)


class Address:
    def __init__(self, name, street_address, city, state, zip_code):
        self._name = name
        self._street_address = street_address
        self._city = city
        self.state = state
        self.zip_code = zip_code
        logging.info('Creating a new address')

    @property
    def name(self):
        return self._name

    @property
    def street_address(self):
        return self._street_address

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        is_state(value)
        self._state = value

    @property
    def zip_code(self):
        return self._zip_code

    @zip_code.setter
    def zip_code(self, value):
        is_zip_code(value)
        self._zip_code = value


class StateError(Exception):
    def __init__(self, value):
        self.value = value
        self.msg = "The state must be in the format of three letters, " \
                   " but Not {}".format(self.value)

    def __repr__(self):
        return self.__class__.__name__

    def __str__(self):
        return self.msg


class ZipCodeError(Exception):
    def __init__(self, value):
        self.value = value
        self.msg = "The zip code must be in the format of NNNNN-NNNN," \
                   " but Not {}".format(self.value)

    def __repr__(self):
        return self.__class__.__name__

    def __str__(self):
        return self.msg


def main():
    parser = OptionParser()

    parser.add_option("-l",             # short option string
                      "--level",        # long option string
                      action="store",   # what to do with the option's argument
                      dest="level",     # where to store the option's argument
                      default="info",   # default value
                      help="Sets the log level to DEBUG, INFO (default), "
                           "WARNING, ERROR, and CRITICAL"
                      )

    parser.add_option("-n",
                      "--name",
                      action="store",
                      dest="name",
                      help="Sets the name value of the Address object"
                      )

    parser.add_option("-a",
                      "--address",
                      action="store",
                      dest="address",
                      help="Sets the address value of the Address object"
                      )

    parser.add_option("-c",
                      "--city",
                      action="store",
                      dest="city",
                      help="Sets the city value of the Address object"
                      )

    parser.add_option("-s",
                      "--state",
                      action="store",
                      dest="state",
                      help="Sets the state value of the Address object"
                      )

    parser.add_option("-z",
                      "--zip_code",
                      action="store",
                      dest="zip_code",
                      help="Sets the zip code value of the Address object"
                      )

    opts, args = parser.parse_args()
    opts_dict = vars(opts)

    # list of options with None values
    lst = [key for key, value in opts_dict.items() if not value]

    if lst:                # if lst is not empty
        parser.error("option(s) {} is/are required.".format(", ".join(lst)))
        # I coudn't know how to access the short string option of an option
        # so I can make the error message to print out the short and long
        # string option so I can tell the user the exact missing option

    if opts.state:
        try:
            is_state(opts.state)
        except StateError:
            parser.error("option -s requires a valid three letters state name")

    if opts.zip_code:
        try:
            is_zip_code(opts.zip_code)
        except ZipCodeError:
            parser.error("option -z requires a valid 5-digit US zip code")

    start_logging(log_file=file,
                  level=opts.level,
                  log_format=formatting)

if __name__ == '__main__':
    main()
