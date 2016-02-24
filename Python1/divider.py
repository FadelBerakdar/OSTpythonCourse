__author__ = 'Fadel'
#!/usr/local/bin/python3

#              The Divider
#               divider.py

# By:        Fadel Berakdar
# Date:      12 Feb 2015


print("Dividing 10 by an integer")

while True :
    num = input("Provide an integer: ")
    if num == "":
        #print("exit")
        break
    try:
        print(10/int(num))
    except ValueError:
        print("Your input must be an integer")
    except ZeroDivisionError:
        print("Your input must not be zero (0)")
    except KeyboardInterrupt :
        print("huh ... no ctrl")

'''

Great job here.

For consideration in future projects ... it's always good to give the user a smooth
way out (typing 'exit', perhaps), especially in a s:/except: block.

FYI, when a user inputs cntl-d a EOFError is generated.  A cntl-c generates a
KeyboardInterrupt Exception.  If your s:/except: block handles both of these
too "smoothly", your user can get really stuck.


-Pat

'''