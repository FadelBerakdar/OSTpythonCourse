#!/usr/bin/env python
# By: Fadel Berakdar
# date: 20 Jan 2016



class Centipede:
    """
    A CLASS
    """
    def __init__(self):
        """
        'super([type[, object-or-type]])
        Return a proxy object that delegates method calls to a parent or sibling
        class of type. This is useful for accessing inherited methods that have
        been overridden in a class. The search order is same as that used by
        getattr() except that the type itself is skipped.'  Docs

        super().__setattr__("stomach", [])
        super().__setattr__("legs", [])

        """

        self.__dict__["stomach"] = []
        self.__dict__["legs"] = []

        # addressing self.__dict__ invokes __getitem__ on an attribute of self,
        # does not invoke __setattr__ on self itself.

    def __call__(self, arg):
        self.stomach.append(arg)

    def __str__(self):
        return ",".join(self.stomach)

    def __repr__(self):
        return ",".join(self.legs)

    def __setattr__(self, key, value):
        if key in ("legs", "stomach"):
            raise AttributeError("{0} is for internal use only".format(key))
        else:
            self.__dict__[key] = value
            self.legs.append(key)