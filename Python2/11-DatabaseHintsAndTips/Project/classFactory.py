#!/usr/bin/env python3
#         **** ClassFactory: function to return tailored classes ****
#                        classFactory.py
# By: Fadel Berakdar
# Date: 28/7/2015


"""
Modify the classFactory.py source code so that the DataRow class returned by
the build_row function has another method:

retrieve(self, curs, condition=None)

self is (as usual) the instance whose method is being called,
curs is a database cursor on an existing database connection,
condition (if present) is a string of condition(s) which must be true of all
received rows.

"""

def build_row(table, cols):
    """ Build a class that create instance of a specific rows. """

    class DataRow:
        """ Generic Data row class, specialized by surrounding function """

        def __init__(self, data):
            """ Uses data and columns names to inject attributes """
            #self.cols = cols
            assert len(data) == len(self.cols)
            self.__dict__.update(zip(self.cols, data))



        def retrieve(self, curs, condition=None):
            if condition:
                curs.execute("SELECT * FROM {0} WHERE {1}".format(self.table,
                                                                  condition))
            else:
                curs.execute("SELECT * FROM {0}".format(self.table))
            for row in curs.fetchall():
                yield DataRow(row)

        def __repr__(self):
            return "{0}_record({1})".format(self.table,
                                            ", ".join(["{0!r}".format(getattr(
                                                self, c)) for c in self.cols]))

    DataRow.table = table
    DataRow.cols = cols.split()
    return DataRow
