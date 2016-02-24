#!usr/bin/env python3
#                  File Counter Test Module
#                   FilesTypesLister.py
# By: Fadel Berakdar
# Date: 25/3/2015

import unittest
import tempfile
import os
import shutil

from FilesTypesLister import lister


class TestFileCounter(unittest.TestCase):
    """A module to test FilesTypesLister.py"""

    def setUp(self):
        """initialize a new directory and create multiple files inside it """
        self.original_dir = os.getcwd()
        self.temporary_dir = tempfile.mkdtemp("test_dir")
        os.chdir(self.temporary_dir)
        os.mkdir("Fake.Directory")
        for file in ["test1.doc",
                     "test2.doc",
                     "long.file.ext.tz",
                     "no_ext",
                     "joe.zip"]:
            open(file, 'w').close()

    def test_files_types(self):
        """test the number of files for each type"""
        expected = {".doc": 2, ".tz": 1, "": 1, ".zip": 1}
        observed = lister(os.getcwd())
        self.assertEqual(observed, expected)

    def tearDown(self):
        """delete the temporary directory and change to the original one."""
        os.chdir(self.original_dir)
        shutil.rmtree(self.temporary_dir)

if __name__ == "__main__":
    unittest.main()

"""
Hi Fadel,

You done a great job on this, generally. The problem you're having is that you
trying to be a little bit too clever.

What could I possibly mean by that? You have chosen to write randomly named
files to the directory. With only ten choices, there's a pretty good chance
that not all of the files_extensions will be represented. In the test method,
your systematically looking for every possibility. When one of the extensions
is missing you get the error.

The root cause here is much more fundamental. You should never have randomly
named anything in your tests method.

Transparency is vitally important when writing tests. If you think about it,
when are people going to look at them? Probably when something is broken, and
probably when they are in a hurry to fix it. You don't want the unfortunate
person trying to find a problem having to work with anything that is obscure,
arcane, or random.

It would be much better to write your tests something like:

def test_working(self):
    for file in ["test1.doc",
                 "test2.doc",
                 "long.file.ext.tz",
                 "no_ext",
                 "joe.zip"]:
        f = open(file, 'w').close()

    expected = {".doc":2, ".tz":1, "":1, ".zip":1}  # dict of expected extensions
    observed = FilesTypesLister.listFiles(os.getcwd())


"""