import re

"""
patternTest.py  Allows the checking of various patterns and target strings
"""

while True:
    pattern = input("Pattern: ")
    if not pattern:
        break
    while True:
        string = input("Target: ")
        if not string:
            break
        mm = re.match(pattern, string)
        if mm:
            print("Match : matched {0!r}".format(string[mm.start():mm.end()]))
            print("Match : groups:", mm.groups())
            print("Match : gdict :", mm.groupdict())

        else:
            print("Match : no match")


        ms = re.search(pattern, string)
        if ms:
            print("Search: matched {0!r}".format(string[ms.start():ms.end()]))
            print("Search: groups:", ms.groups())
            print("Search: gdict :", ms.groupdict())
        else:
            print("Search: no match")


