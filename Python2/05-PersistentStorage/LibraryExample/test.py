import shelve

shelf = shelve.open("e_coli")

shelf["species"] = "coli"
shelf["genus"] = "Esherishia"
shelf["version"] = 123123

print([key for key in shelf.keys()])
print(shelf.keys())
for i in shelf.k


shelf.close()



