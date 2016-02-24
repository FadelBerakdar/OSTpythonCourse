#!usr/bin/env python3
#                  File Counter Module
#                   FilesTypesLister.py
# By: Fadel Berakdar
# Date: 25/3/2015


import os
import glob


def lister(path="."):
    """A module which returns a dictionary of the existing files in a directory
    and the number of each file type"""

    files = {}
    for i in glob.glob(os.path.join(path, "*")):
        if os.path.isfile(i):  # no directories are listed
            if os.path.splitext(i)[1] in files.keys():
                files[os.path.splitext(i)[1]] += 1
            else:
                files[os.path.splitext(i)[1]] = 1
    return files

'''
import glob
import os

"""write a module containing a function to examine the contents of the current working directory and
    print out a count of how many files have each extension (".txt", ".doc", etc.)"""

def print_extension(path="."):
    ext_dict = {}

    files = glob.glob(os.path.join(path, "*"))
    ext_files = [os.path.splitext(fn) for fn in files]
    ext = [ext for (name, ext) in ext_files]

    for each in ext:
        if ext_dict.__contains__(each):
            ext_dict[each] += 1
        else:
            ext_dict[each] = 1

    return ext_dict
'''