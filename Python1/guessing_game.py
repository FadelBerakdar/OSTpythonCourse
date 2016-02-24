#!/usr/local/bin/python3

#            Guessing Game
#            guessing_game.py

# By:        Fadel Berakdar
# Date:      25 Jan 2015

#!/usr/local/bin/python3

#            Guessing Game
#            guessing_game.py

# By:        Fadel Berakdar


import random


number= random.randint(1,99)
guess = ""


while(guess != number ):
    guess = input("Guess a number: ")

    if guess.isdigit():
        guess = int(guess)
        if (guess < number):
            print("Too low")
        elif(guess > number):
            print("Too high")
        else :
            print("You guessed it!")
    else:
        print("Pls enter an integer ")

"""
user$ conda install -c https://conda.anaconda.org/vgauthier graph-tool
Fetching package metadata: ......
Solving package specifications: ..........................
Error: Could not find some dependencies for graph-tool: cairomm, sigcpp

Did you mean one of these?

    graph-tool

Did you mean one of these?

    cairomm, cairo, pycairo

You can search for this package on anaconda.org with

    anaconda search -t conda sigcpp

 (and similarly for the other packages)


user$ brew list cairomm
/usr/local/Cellar/cairomm/1.12.0/include/cairomm-1.0/ (22 files)
/usr/local/Cellar/cairomm/1.12.0/lib/libcairomm-1.0.1.dylib
/usr/local/Cellar/cairomm/1.12.0/lib/cairomm-1.0/include/cairommconfig.h
/usr/local/Cellar/cairomm/1.12.0/lib/pkgconfig/ (9 files)
/usr/local/Cellar/cairomm/1.12.0/lib/libcairomm-1.0.dylib
/usr/local/Cellar/cairomm/1.12.0/share/devhelp/books/cairomm-1.0/cairomm-1.0.devhelp2
/usr/local/Cellar/cairomm/1.12.0/share/doc/ (216 files)

user$ brew list libsigc++
/usr/local/Cellar/libsigc++/2.6.2/include/sigc++-2.0/ (33 files)
/usr/local/Cellar/libsigc++/2.6.2/lib/libsigc-2.0.0.dylib
/usr/local/Cellar/libsigc++/2.6.2/lib/pkgconfig/sigc++-2.0.pc
/usr/local/Cellar/libsigc++/2.6.2/lib/sigc++-2.0/include/sigc++config.h
/usr/local/Cellar/libsigc++/2.6.2/lib/libsigc-2.0.dylib
/usr/local/Cellar/libsigc++/2.6.2/share/devhelp/books/libsigc++-2.0/libsigc++-2.0.devhelp2
/usr/local/Cellar/libsigc++/2.6.2/share/doc/ (600 files)
"""