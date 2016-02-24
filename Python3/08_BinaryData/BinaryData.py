#!/usr/bin/env python
# By: Fadel Berakdar
# Date: 24 Nov 2015

import os
import struct
import random

" floattest.py: demonstrate use of floating-point values in files. "


# The bytes and bytearray objects allow you to map the individual bytes of a
# file's contents, or of a sequence of bytes read over the network.

# The struct module allows you to interpret these values as the computer's basic
# data types—bytes, integers, and floating-point numbers.





rlist = [random.random() for i in range(10)]
print("rList = ",rlist)


f = open("newFile", "wb")
f.write(struct.pack("=10d", *rlist))
f.close()
f = open("newFile", "rb")


for i in range(10):
    s = f.read(8)
    x, = struct.unpack("=d", s)  # x, = (1,) the tuple contains one element
    if x != rlist[i]:
        print(i, x, rlist[i], abs(x-rlist[i]))
    else:
        print(i, x, "values agree")
print("newFile", os.stat("newFile").st_size)
f.close()




