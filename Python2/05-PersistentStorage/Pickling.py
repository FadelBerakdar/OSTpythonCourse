__author__ = 'Fadel'

import pickle

obj1 = [1, 2, 3, 4, 5]
obj2 = "Hey there!"

output = open("Objects.pkl", "wb")
pickle.dump(obj1, output)
pickle.dump(obj2, output)
output.close()

input = open("Objects.pkl", "rb")
print(pickle.load(input))
'''
obj1 = [1, 2, 3, 4, 5]
obj2 = "Hey there!"

output = open("Objects.pkl", "wb")
pickler = pickle.Pickler(output)
pickler.dump(obj1)
pickler.dump(obj2)
output.close()

input = open("Objects.pkl", "rb")
unpickler = pickle.Unpickler(input)
obj11 = unpickler.load()
obj22 = unpickler.load()
'''

