#!usr/bin/env python3
#                  Testing Module
#                TestHighestScore.py
# By: Fadel Berakdar
# Date: 30 July 2015

"""
import unittest
import glob
import os
import shutil
import tempfile
import archive


class TestArchive(unittest.TestCase):

    def setUp(self):
        self.ori_dir = os.getcwd()
        self.new_dir = tempfile.mkdtemp()
        os.chdir(self.new_dir)
        self.file_names1 = ["Readme.txt", "setup", "system"]
        for fn in self.file_names1:
            open(fn, "w").close()

        self.new_new_dir = tempfile.mkdtemp()
        os.chdir(self.new_new_dir)
        self.file_names2 = ["final.pdf", "second"]
        for fn in self.file_names2:
            open(fn, "w").close()

    def test(self):
        observed = archive.zip_me3(self.new_dir)
        expected = []
        for fn in glob.glob(os.path.join(self.new_dir, "*")):

            if os.path.splitext(fn)[1] != ".zip" and os.path.isfile(fn):
                expected.append(fn[1:])  # .replace("/","\\")
        self.assertEqual(observed, expected, "something went wrong -_-")

    def tearDown(self):
        os.chdir(self.ori_dir)
        shutil.rmtree(self.new_dir)

if __name__ == "__main__":
    unittest.main()


import unittest
from archive import dirArchive
import os, shutil

class TestRelativezip(unittest.TestCase):
    filenames = ["groucho", "harpo", "chico"]
    path = "v:\\workspace\\Python2_Homework05\\src\\archive_me"

    def setUp(self):
        # Make test files to compress
        os.mkdir(self.path)
        for fn in self.filenames:
            f = open(os.path.join(self.path, fn), "w")
            f.close()
        # Make test subdirectory and subdirectory files
        os.mkdir(self.path + "\\subdir")
        for fn in self.filenames:
            f = open(os.path.join(self.path + "\\subdir", fn), "w")
            f.close()

    def test_relativezip(self):
        dirArchive(self.path)

    def tearDown(self):
        shutil.rmtree(self.path)
        os.remove(self.path + ".zip")

if __name__ == "__main__":
    unittest.main()
"""