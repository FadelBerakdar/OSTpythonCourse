import os, glob, shutil, tarfile, zipfile

file_names = ["heyworld","setup","readme"]
path = "/Users/Fadel/Dropbox/python/Code/Python2/06-Archives/test"

try :
    os.mkdir(path)
except:
    pass


for fn in file_names:
    open(os.path.join(path,fn),"w").close()
print(glob.glob(os.path.join(path,"*")))

zf  = zipfile.ZipFile(os.path.join(path,"zip_file.zip"),"w", zipfile.ZIP_DEFLATED)
print(zf.namelist())
print(os.path.getsize(os.path.join(path,"zip_file.zip")))

for fn in glob.glob(os.path.join(path,"*")):
    zf.write(fn)
print(zf.namelist())
print(os.path.getsize(os.path.join(path,"zip_file.zip")))

zf.close()
shutil.rmtree(path)

