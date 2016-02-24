
#!/usr/bin/env python3

#              Demo test
#             setupDemo.py.p
# By: Fadel Berakdar
# Date: 19 Mar 2015


"""
Demonstration of setUp/tearDown.
The tests do not actually test anything much - this is a demo.
"""
import unittest
import tempfile
import shutil
import glob
import os


class FileTest(unittest.TestCase):

    def setUp(self):
        """initialize a new temporary directory."""
        self.origdir = os.getcwd()
        self.dirname = tempfile.mkdtemp("test_dir")


        os.chdir(self.dirname)

    def test_1(self):
        """Verify the exact file are existed"""
        file_names_set = {'that.txt', 'the_other.txt', 'this.txt'}
        for filename in file_names_set:
            open(filename, "w").close()
        self.assertEqual(set(os.listdir()), file_names_set)

    def test_2(self):
        """Verify that the current directory is empty"""
        self.assertEqual(glob.glob("*"), [], "Directory not empty")

    def test_3(self):
        """"Verify that the binary file size equals 1000000 bytes"""
        binary_file = open("binary_file", "wb")
        file_size = 1000000
        binary_file.write(b"1" * file_size)
        binary_file.close()
        self.assertEqual(os.stat("binary_file")[6], file_size,
                         "The file size should be equal to {} bytes!"
                         .format(file_size))

    def tearDown(self):
        """change the directory to the original and delete the temporary one"""
        os.chdir(self.origdir)
        shutil.rmtree(self.dirname)



if __name__ == "__main__":
    unittest.main()
'''
Expected type 'bytes | str', got 'FileIO[bytes]' instead less... (⌘F1)
This inspection detects type errors in function call expressions. Due to

dynamic dispatch and duck typing, this is possible in a limited but useful
number of cases. Types of function parameters can be specified in docstrings
or in Python 3 function annotations.


Hi Fadel,

I hope you're having a good day.

You've done a great job on this project. Your project works just great.

Unfortunately, I have to turn it back because successful tests should be
(nearly) silent. You'll want to lose the print () statements or find a way
 to execute them conditionally. Here's a trick:

DEBUG=True
if DEBUG: print("Created", self.dirname)

... the right way to handle this is with logging, which we get into
an (OST) Python 3

Here are a few tips and tricks that you may find useful:

-If you don't care what's in the file, you don't need to write to it.
 And if you're not going to do anything with it, you don't even need a
 handle for it.  So for this project, you could create a file that simply as:

open('myfile', 'w').close()

-Sorting the lists works, but so would using set objects.

-Whenever you find yourself typing something more than once, you'll want
to ask yourself whether or not there is an easy way to create a variable
 instead. The test_3() method is a case in point. You had to type some
  permutation of "1 million" more than once. It's borderline-trivial for
  the small exercise, but imagine a larger effort with a lot more code ...
  If the project specifications were changed from 1,000,000 to 2,000,000,
  you'll be potentially set up for a maintenance nightmare.


-Pat
'''


