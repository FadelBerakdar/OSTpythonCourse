__author__ = 'Fadel'
#!/usr/bin/env python3

#              unittest test program for semi-title() function
#                        bunch_class
# By: Fadel Berakdar
# Date: 23 Feb 2015


import string
import sys


def length_counter(name):
    print("{0:>65}\n{1:>60}\n{0:>65}".format(50 * "*", "Welcome to word length counter module."))
    print("\n{} Fact Sheet: ".format(name))

    file = open(name, "r")
    lines = file.readlines()  # reading the whole file once
    counter_dict = {}  # initialising a new dictionary for length-count pairs

    for line in lines:  # looping over the lines
        for word in line.split():  # looping over the words
            word = word.strip()
            word = "".join(letter for letter in word if letter not in string.punctuation + "&")
            if counter_dict.get(len(word)):  # updating the existing elements in the dictionary
                counter_dict[len(word)] += 1
            else:
                counter_dict.update({len(word): 1})  # adding new elements in the dictionary
    print("")
    print("{:<7}{}".format("Length", "Occurrences"))
    for key, value in sorted(counter_dict.items()):  # printing the dictionary elements
        print("{:=3}{:=7}".format(key, value))

    file.close()
    print("\n", 40 * "=", "\n")

    value_max = max(counter_dict.values())

    for key, value in counter_dict.items():  # I think I should omit this step, but I couldn't know how!
        value = str(value * "•") + str((value_max-value) * " ")
        counter_dict[key] = value

    y = len(max(counter_dict.values()))  # initialising a variable to refer to the maximum value in the dictionary

    if y >= 100:  # initialising a variable to decide the approximation factor
        approx = 100
    else:
        approx = 10

    y -= y % - approx  # round y to the next approx

    print(" words\ncounter")
    while y > 0:  # looping over the dictionary
        print("{:=4} | ".format(y), end=" ")
        for x in range(1, max(counter_dict.keys()) + 1):
            if y in range(0, len(max(counter_dict.values()))):
                if counter_dict.get(x):
                    print(counter_dict.get(x)[y-1], end="  ")
                else:
                    print("   ", end="")
        print("")
        y -= (approx//10)

    print("     +--" + "+--"*max(counter_dict.keys())+">  words Length")
    x = 0
    print("    ", end="")
    while x <= max(counter_dict.keys()):
        print("{:<2}".format(x), end=" ")
        x += 1
    print("\n\n\n{:>60}".format(20*"*" + "The end" + 20*"*"))

if __name__ == "__main__":
    try:
        if len(sys.argv) == 2:  # sys.argv returns a tuple of the module passed arguments
            length_counter(str(sys.argv[1]))
        else:
            print("Dear User! This module accepts exactly one arguments\nExample: python3 final.py file.txt")
    except FileNotFoundError:
        print("Dear User!  Please pass a correct file name.\nExample: python3 {} file.txt ".format(sys.argv[0]))