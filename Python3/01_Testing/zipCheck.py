#!/usr/bin/env python

# zipcheck.py: validation function for US zip codes
# By: Fadel Berakdar
# Date: 1 Oct 2015

"""
US Zip code problem:
    * The zip code must be a string of length five or ten characters
    * The first five must be numeric
    * if the length of the string is ten, the sixth character must be a
         minus sign and the last four must be numeric.

"""

def zip_errors(z):
    """
    Validate z as either NNNNN or NNNNN-NNNN
    return None when the conditions are met
    """

    if len(z) not in (5, 10):
        return "zip code must be five or ten digits"

    if not z[:5].isdigit() or (len(z) == 10 and not z[6:].isdigit()):
        return "Zip code has non-numeric characters"

    if len(z) == 10 and z[5] != "-":
        return "Ten-digit zips must have a dash between the two parts"

    return None

