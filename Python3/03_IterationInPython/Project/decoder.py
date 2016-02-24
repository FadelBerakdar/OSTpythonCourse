#!/usr/bin/env python

# By: Fadel Berakdar
# Date: 10 Nov 2015


class Alphabator(object):
    """
    Iterator class which takes list and returns a list of the same elements
    unless the element is between 1~26, in that case the element is replaced by
    its equivalent ascii character
    """
    def __init__(self, lst):
        self.lst = lst
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            if self.lst[self.index] in range(1, 27):
                x = chr(self.lst[self.index]+64)
            else:
                x = self.lst[self.index]
        except IndexError:
            raise StopIteration
        self.index += 1
        return x


def normal(lst):
    """
    normal approach
    """
    numbers = [x for x in range(1, 27)]
    new = []
    for i in lst:
        if i in numbers:
            new.append(chr(i+64))
        else:
            new.append(i)
    return new


def generator(lst):
    for i in lst:
        if i in range(1, 27):
            x = chr(i+64)
        else:
            x = i
        yield x
