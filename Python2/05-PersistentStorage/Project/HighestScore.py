#!usr/bin/env python3
#                  Highest Score Recorder Module
#                             HighestScore.py
# By: Fadel Berakdar
# Date: 3/5/2015

import shelve


def high_score(name=str, score=int):
    """function which takes two arguments (player, score) and keeps
    high score table in python shelve"""

    shelf = shelve.open("Records")
    if name in shelf:
        if shelf[name] < score:
            shelf[name] = score
    else:
        shelf[name] = score
    highest = shelf[name]
    shelf.close()
    return highest


def high_score2(name=str, score=int):
    shelf = shelve.open("Records")
    # I don't know if we can use s,except in this case
    try:
        if shelf[name] < score:
            shelf[name] = score
    except:  # too broad exception, I couldn't know how to minimize it.
        shelf[name] = score
    highest = shelf[name]
    shelf.close()
    return highest


def high_score3(name=str, score=int):
    shelf = shelve.open("Records")
    if (name in shelf and shelf[name] < score) or (name not in shelf):
        shelf[name] = score
    highest = shelf[name]
    shelf.close()
    return highest
