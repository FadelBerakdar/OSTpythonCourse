#!usr/bin/env python3
#                  Archiving Directory Module
#                       archive.py
# By: Fadel Berakdar
# Date: 3/5/2015


import zipfile
import os
import glob

"""
The zipfile example in the lesson text stores the full path of the files that
it saves to the zipfile. Normally, however, zipfiles contain only a relative
pathname (you will see that when the names are listed after the zipfile is
created, the "v:\\" has been removed).

Create a project named Archives_Homework and add it to the Python2_Homework
\working set. In this project, write a function that takes a directory path
and creates an archive of the directory only. For example, if the same path
were used as in the example ("v:\\workspace\\Archives\\src\\archive_me"),
the zipfile would contain "archive_me\\groucho" "archive_me\\harpo" and
"archive_me\\chico."

Note that zipfile.namelist() always uses forward slashes in what it returns,
a fact you will need to accommodate when comparing observed and expected.

The base directory ("archive_me" in the example above) is the final element of
the input, and all paths recorded in the zipfile should start with the base
directory.

If the directory contains subdirectories, the subdirectory names and any files
in the subdirectories should not be included. (Hint: You can use isfile()
to determine if a filename represents a regular file and not a directory.)

"""

def zip_me(path="."):
    """ a function that takes a directory path and creates an archive of
     the directory only """

    zf = zipfile.ZipFile(os.path.join(path, "zip_dir.zip"),
                         "w", zipfile.ZIP_DEFLATED)

    for fn in glob.glob(os.path.join(path, "*")):
        if os.path.isfile(fn):
            if os.path.splitext(fn)[1] != ".zip":
                zf.write(fn)
    zf.close()
    return zf.namelist()


def zip_me2(path="."):
    zf = zipfile.ZipFile(os.path.join(path, "zip_dir.rar"),
                         "w", zipfile.ZIP_DEFLATED)

    for fn in glob.glob(os.path.join(path, "*")):
        print("considering", fn , end="  ")

        if os.path.isfile(fn):#  and not zipfile.is_zipfile(fn):
            if zipfile.is_zipfile(fn):
                print("Ok")
                zf.write(fn)
            else:
                print("nope")
        else:
            pass
            print("nope")
    zf.close()
    return zf.namelist()

def dirArchive(path):
    basedir = os.path.dirname(path)
    relativedir = os.path.basename(path)

    startPath = os.curdir
    os.chdir(basedir)

    # Select files to compress
    filenames = glob.glob(os.path.join(relativedir, "*"))
    for fn in filenames:
        if not os.path.isfile(basedir + '\\' + fn):
            filenames.remove(fn)

    # Make archive and compress files
    archive_fn = path + ".zip"
    zf = zipfile.ZipFile(archive_fn, "w")
    for fn in filenames:
        zf.write(fn)
    zf.close()
    os.chdir(startPath)

