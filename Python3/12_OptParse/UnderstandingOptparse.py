#!/usr/bin/env python

from optparse import OptionParser

"""
UnderstandingOptparse.py: a try to understand optparse library
"""
if __name__ == "__main__":
    parser = OptionParser()
    parser.add_option("-l",             # short option string
                      "--loglevel",     # long option string
                      action= "store",  # what to do with the option's argument
                      type="string",    # the type of accepted option's argument
                      dest="level",     # where to store the option's argument
                      default="warning",  # default value
                      help="set level of logger"
                      )

    parser.add_option("-p",
                      action="store_true",  # to set boolean variable
                      dest="value")
    parser.add_option("-q",
                      action="store_false",
                      dest="value")

    opts, args = parser.parse_args()

    # an object containing values for all of your options
    print("Options", opts)

    # args are the list of positional arguments leftover after parsing options
    print("Arguments", args)

    print(opts.level)
    print(opts.value)