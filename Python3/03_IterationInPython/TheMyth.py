# Containers Vs Iterables Vs Iterators Vs Generators
# http://nvie.com/posts/iterators-vs-generators/
# https://www.youtube.com/watch?v=LelQTPiH3f4


# Containers are data structures holding elements, and that support membership
# tests. like list, set, dict, tuple, strings

lst = [1, 3, 4, 5]
string = "ABC"

assert 1 in lst
assert "A" in string

# Iterable is any object, not necessarily a data structure, that can return an
# iterator (with the purpose of returning all of its elements).
# most containers are iterable objects
# iterable supports the dunder method __iter__()


x = [0, 2, 4]  # here x is an iterable
y = iter(x)    # here y is an iterator

x.__iter__()  # thus its iterable
y.__next__()  # thus its iterator

# Iterator is a stateful helper object that will produce the next value when you
# call next() on it.
# Any object that has a __next__() method is therefore an iterator.
# So an iterator is a value factory. Each time you ask it for "the next" value,
# it knows how to compute it because it holds internal state.
# iterator supports the dunder method __next__()
"""
Central idea: a lazy factory
From the outside, the iterator is like a lazy factory that is idle until you ask
it for a value, which is when it starts to buzz and produce a single value,
after which it turns idle again
"""

# Producing infinite sequences from finite sequences
from itertools import cycle

colors = cycle(["red", "white", "blue"])
colors.__next__()
next(colors)
next(colors)
next(colors)
next(colors)
print(next(colors))

# Producing finite sequence from infinite sequence
from itertools import cycle, islice

colors = cycle(["red", "white", "blue"])
finite = islice(colors, 0, 4)
for color in finite:
    print(color)


class Fib:
    def __init__(self):
        self.prev = 0
        self.curr = 1

    def __iter__(self):   # so this class is an iterable
        return self

    def __next__(self):   # so this class is an iterator
        value = self.curr
        self.curr += self.prev
        self.prev = value
        return value

fibo = Fib()
print(list(islice(fibo, 0, 10)))


# Generator is
# a special kind of iterator
# a factory that lazily produces values
# its either a function with yield statement or generator expression

# why to use generators:
# They allow us to write streaming code with fewer intermediate variables and data structures.
# they are more memory and CPU efficient.
# they tend to require fewer lines of code.

def fib():
    prev, curr = 0, 1
    while True:
        yield curr
        prev, curr = curr, prev+curr

newfibo = fib()
print(list(islice(newfibo, 0, 10)))
