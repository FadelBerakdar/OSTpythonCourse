__author__ = 'Fadel'

#!usr/bin/env python3

# Tar Module



import tarfile
import os
import glob
import shutil

file_names = ["Larry", "Curly", "mow"]
path = "/Users/Fadel/Dropbox/python/Code/Python2/06-Archives/test"


try :
    os.mkdir(path)
except:
    pass



for file in file_names:
    open(os.path.join(path,file),"w").close()

#initializing a tar file without compression

tf = tarfile.open(os.path.join(path,"tarfile.tar"),"w")
tf.add(path)
tf.list()
tf.close()
print(os.path.getsize(os.path.join(path,"tarfile.tar")))
print(20 * "=")

#initializing a tar file with
tf = tarfile.open(os.path.join(path,"tarfile.tar.gz"),"w:gz")
tf.add(path)
tf.list()
tf.close()
print(os.path.getsize(os.path.join(path,"tarfile.tar.gz")))


#avoide adding the whole directory
tf = tarfile.open(os.path.join(path,"tarfile_2.tar.gz"),"w:gz")

for i in glob.glob(os.path.join(path,"*")):
   if os.path.splitext(i)[1] not in [".tar",".gz"]:
       tf.add(i)
tf.list()
tf.close()
print(os.path.getsize(os.path.join(path,"tarfile_2.tar.gz")))

shutil.rmtree(path)
