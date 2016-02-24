
""" Injecting attributes to an object """
# Injecting columns names as attributes
# and the rows as values of those attributes
# 4 ways:
# obj.Name1 = "value1"
# obj.__dict__.update(dict(zip(["Name2"],["value2"])))
# setattr(obj,"Name3", "Value3")


columns = "ID Name Email".split()
data = (1, "Steve", "steve@ost.com")


class Row(object):
    pass


# setters:
r1 = Row()
for column, dat in zip(columns, data):
    setattr(r1, column, dat)

print(dir(r1)[0:3])

# __dict__:
r2 = Row()
r2.__dict__.update(dict(zip(columns, data)))
print(dir(r2)[0:3])

# class:
# a class with a constructor call that takes the column names and data items as
# arguments, and returns an object with the attributes set.


class RowClass(object):
    def __init__(self, cols, dataa):
        self.__dict__.update(zip(cols, dataa))

    def __repr__(self):
        return "user_record(ID: {0.id}, Name: {0.name}, Email: {0.email})" \
               "".format(self)

r3 = RowClass(columns, data)
print(dir(r3)[0:3])


#        *** Class with the column names already incorporated ***
#            class Factory Function to return tailored classes
# By constructing the class inside a function, which takes the column and
# the table names as arguments. The function then returns the class after
# inserting the table name and the column names as class attributes.
# The function effectively becomes a "class factory," returning a slightly
# different class each time it is called.

def build_row(table, columns):
    """Build a class that creates an instance of specific rows. """

    class DataRow(object):
        """ Generic data row class, specialized by surrounding function  """

        def __init__(self, data):
            """ Uses data and columns names to inject attributes"""
            assert len(data) == len(self.columns)
            self.__dict__.update(zip(self.columns, data))

        def __repr__(self):
            return "{0}_record {1}".format(self.table, ", ".join(["".format(getattr(self, c) for c in self.columns)]) )

    DataRow.table = table
    DataRow.columns = columns
    return DataRow
