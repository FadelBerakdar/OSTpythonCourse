


class Bunch(object):
    """
    More secure bunch class
    """
    def __init__(self, *args, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __setattr__(self, key, value):
        """
        in this way, we will check the instance.__dict and the class.__dict
        whenever the used add new attribute
        """
        if hasattr(self, key) or hasattr(self.__class__, key):
            raise AttributeError("already got this attribute: {}".format(key))
        else:
            self.__dict__[key] = value

    def pretty(self):
        text = ""
        for key, value in self.__dict__.items():
            text += "{} {} \n".format(key, value)
        return text


class Book(Bunch):
    pass

if __name__ == "__main__":

    a = Book(name="fadel",email="afad@asda")
    print(a.pretty())
    a.pretty = 1
    print(a.pretty)