#!/usr/bin/env python
# By: Fadel Berakdar
# date: 22 Jan 2016

import re


class Address:
    def __init__(self, name, street_address, city, state, zip_code):
        self._name = name
        self._street_address = street_address
        self._city = city
        self.state = state
        self.zip_code = zip_code

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
            raise StateError(value)

    @property
    def zip_code(self):
        return self._zip_code

    @zip_code.setter
    def zip_code(self, value):
        if re.match(r"\d{5}$", value):
            self._zip_code = value
        else:
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
        #self.msg = "The zip code must be in the format of five numbers NNNNN," \
                   #" but Not {}".format(self.value)

    def __repr__(self):
        return self.__class__.__name__

    def __str__(self):
        return self.__class__.__name__
        #return self.msg

home = Address(name="Steve Holden",
                            street_address="1972 Flaying Circus",
                            city="Arlingtonn",
                            state="VA",
                            zip_code="12345")

class OhMyGoodnessExc(Exception):
    def __init__(self):
        Exception.__init__(self,"well, that rather badly didnt it?")
raise OhMyGoodnessExc