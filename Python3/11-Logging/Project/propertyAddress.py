#!/usr/bin/env python
# By: Fadel Berakdar
# date: 23 Jan 2016

import re
import logging


class Logging:
    def start_logging(file_name="propertyAddress.log", level="error"):
        """
        Start logging with given filename and level.
        :param file_name: the log file name
        :param level: the level of built-in logger functions
        :return: None
        """

        #log_format = "%(asctime)s - %(levelname)s - %(funcName)10s - %(message)s"
        log_format = "{} - {} - {} - {}".format(asctime, levelname, funcName, message)

        levels = {'debug': logging.DEBUG,
                  'info': logging.INFO,
                  'warning': logging.WARNING,
                  'error': logging.ERROR,
                  'critical': logging.CRITICAL}

        logging.basicConfig(filename="propertyAddress",
                            level=logging.INFO,
                            format=log_format)
        logging.info('Starting up the propertyAddress program')  # log a message



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

        if re.match(r"[A-Z]{2}$", value):
            self._state = value
        else:
            logging.error("State exception")
            raise StateError(value)

    @property
    def zip_code(self):
        return self._zip_code

    @zip_code.setter
    def zip_code(self, value):
        if re.match(r"\d{5}$", value):
            self._zip_code = value
        else:
            logging.error("ZIPCODE exception")
            raise ZipCodeError(value)


class StateError(Exception):
    def __init__(self, value):
        self.value = value
        self.msg = "The state must be in the format of two letters, " \
                   " but Not {}".format(self.value)

    def __repr__(self):
        return self.__class__.__name__

    def __str__(self):
        return self.msg


class ZipCodeError(Exception):
    def __init__(self, value):
        self.value = value
        self.msg = "The zip code must be in the format of five numbers NNNNN," \
                   " but Not {}".format(self.value)

    def __repr__(self):
        return self.__class__.__name__

    def __str__(self):
        return self.msg



