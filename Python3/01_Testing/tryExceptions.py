
import math

while True:
    try:
        text = input('> ')
        if text[0] == 'q':
            break
        x = float(text)
        y = math.log10(x)
        print("log10({0}) = {1}".format(x,y))
    except ValueError:
        print("The Value must be greater than 0")