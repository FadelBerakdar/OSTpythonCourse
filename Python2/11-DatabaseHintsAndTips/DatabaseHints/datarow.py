# Using Class:
# Implements a simple data record class


class Row(object):
    def __init__(self, columns, data):
        self.__dict__.update(zip(columns, data))

    def __repr__(self):
        return "user_record(id={0.id} name={0.name} email={email})".format(self)

if __name__ == "__main__":
    r1 = Row(['id', 'name', 'email'], [1, "Steve", "steve@"])
    if r1.id != 1 or r1.name != "Steve" or r1.email != "steve@":
        print("TEST FAILED: id={0.id} name={0.name} email={email})".format(r1))
    else:
        print("every thing is good")
