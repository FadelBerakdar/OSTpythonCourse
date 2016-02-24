# what's the difference between a regular function and a generator function?

# The answer is that calling a generator function produces a special type of
# iterator object (a "generator"). The function namespace is created and
# initialized with the argument values. The function code only starts executing
# with the first call to the generator's __next__() method.Execution continues
# until a yield expression is evaluated:the value ofthe expression following
# yield becomes the value of the __next __() method call. You can see this with
# a very simple generator function in an interactive session.

"""
Suppose you need to produce sequences determined by a list, but need to repeat
the first list element once, the second twice, and so on. So given a list
[2, 4, 6], the resulting sequence would be 2, 4, 4, 6, 6, 6. Let's write a
generator that produces such sequences. First, though, we'll write tests to
ensure that our generator function works:
"""


def normal(lst):
    new = list()
    for index, element in enumerate(lst):
        for i in range(index+1):
            new.append(element)
    return new


def generator(lst):
    for index, element in enumerate(lst):
        for i in range(index+1):
            yield element



class Iterator(object):
    def __init__(self, lst):
        self.lst = lst
        self.index = 0
        self.counter = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter > self.index:
            try:
                self.value = self.lst[self.index]
            except IndexError:
                raise StopIteration
            self.index += 1
            self.counter = 1
        self.counter += 1
        return self.value


# Testing suite
import unittest


class TestNormal(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(normal([]), [])

    def test_real_Work(self):
        self.assertEqual(normal([1]), [1], "[1] does not give [1]")
        self.assertEqual(normal([1, 2]), [1, 2, 2])
        self.assertEqual(normal([1, 2, 3]), [1, 2, 2, 3, 3, 3])


class TestGenerator(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(list(generator([])), [])

    def test_real_Work(self):
        self.assertEqual(list(generator([1])), [1], "[1] does not give [1]")
        self.assertEqual(list(generator([1, 2])), [1, 2, 2])
        self.assertEqual(list(generator([1, 2, 3])), [1, 2, 2, 3, 3, 3])


class TestIterator(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(list(Iterator([])), [])

    def test_real_Work(self):
        self.assertEqual(list(Iterator([1])), [1], "[1] does not give [1]")
        self.assertEqual(list(Iterator([1, 2])), [1, 2, 2])
        self.assertEqual(list(Iterator([1, 2, 3])), [1, 2, 2, 3, 3, 3])


if __name__ == "__main__":
    unittest.main()
