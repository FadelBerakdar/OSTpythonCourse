__author__ = 'Fadel'

#!/usr/local/bin/python3

#              Dogs List
#             doggies.py.

# By:        Fadel Berakdar
# Date:      13 Feb 2015



class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed


dogs = [] #initializing an empty list called dogs

while True:
    name = input("Name: ")
    if name:     #checking the input
        breed = input("Breed: ")
        dogs.append(Dog(name, breed))
        print("DOGS")
        for index, dog in enumerate(dogs):
            print(index,". ",dog.name,": ", dog.breed)                      #
        print("*"*40)
    else :
        break


'''
Hi Fadel,

Okay, let's see how close to perfection I can get (I'm not so hopeful, but here it goes)  ;-)

This is really close to being correct. The idea here is that the app is supposed to
append an intact instance of the Dog class. In other words, you want to append the dog
object created here:

dog = Dog("","")

... As opposed to a pending the name and breed attributes.

Here are a few (optional) tips/observations:

-You might consider using this idiom:

if not dog.name:

... Instead of this one, for readability:

if dog.name != "":

 - If you want, you could directly create an instance of Dog with your input instead of
  creating an instance with placeholder values then filling them in:

dog=Dog(name, breed)

... and to consolidate things further, you could create the instance and appended in
the same line of code:

dogs.append(Dog(name, breed))

- While it's okay to create a main() method, you really don't have to.
The  if __name__=='__main__':  block of code will get executed when this program is
run in a stand-alone mode (but not when it's imported into another module) - so it is typically
used to stash code that is used for local testing, etc. There's no particular need for the
additional complexity here.

-Per the as style manual (PEP-8), you would want to make this into 2 separate lines.
Instead of:

if __name__ == "__main__":main()

... you would want to go:

if __name__ == "__main__":
       main()

The fix should be easy.

-Pat
'''