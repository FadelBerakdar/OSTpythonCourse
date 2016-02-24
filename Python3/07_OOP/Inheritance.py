# Inheritance

class Parent:
    skin_color = "green"


class Child1(object):
    pass


class Child2(Parent):
    skin_color = "blue"

# __dict__ stores the class attributes only without its bases classes
print(sorted(list(Child1.__dict__)))
# dit() returns the attributes of the class and its base classes
print(sorted(dir(Child1)))

# Method Resolution Order
# look for an attribute in  --->> instance namespace
#                           --->> class namespace
#                           --->> bases classes one by one from the left
print(Child1.__mro__)


# Multiple Inheritance
class Mother(object):
    hair_color = "Blond"
    temperament = "placid"


class Father(object):
    hair_color = "ginger"
    curiosity = "high"


class Daughter(Mother, Father):
    pass

print(Daughter.hair_color)  # the base classes are searched left-to- right.
