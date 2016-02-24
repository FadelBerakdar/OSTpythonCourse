#!/usr/bin/env python


""" Demonstrate how to make instances callable. """
class funclike:
    """
    Im plem enting the __call__( )  method allows  you to  m ake your instances
    callable
    """

    def __call__(self, *args, **kwargs):
        print("Args are:", args)
        print("Kwargs are:", kwargs)


f = funclike()
f(1, 2, 3, this="one", that="the other")