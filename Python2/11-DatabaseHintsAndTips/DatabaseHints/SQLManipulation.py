
# import mysql.connector
# from database import login_info

table = "Animal"
columns = "id name family"
conditions = ["id=7"]

query = "SELECT {0} FROM {1} WHERE {2}".format(", ".join(columns.split()),
                                                         table,
                                                         conditions[0]
                                               )




class Row():
    pass


columns = "ID Name Email".split()
data = (1, "Steve", "steve@steveholden.com",)

r1 = Row()
for column, dat in zip(columns, data):
    setattr(r1, column, dat)
print("r1 attributes", r1.ID, r1.Name, r1.Email)


r2 = Row()
r2.__dict__.update(dict(zip(columns,data)))
print("r2 attributes", r2.ID, r2.Name, r2.Email)


class NewRow(object):
    def __init__(self, ID, Name, Email):
        self.ID = ID
        self.Name = Name
        self.Email = Email

r2 = NewRow(2, "John", "Joh@gmail.com")

#print(bool(dir(r1) == dir(r2)))

print(dict(zip(columns,data)))
