#zip
from zipfile import*
f = ZipFile("D:/Rohit123/xyz.zip","w",ZIP_DEFLATED)
f.write("abc.txt")
f.write("pqr.txt")
f.close()
print("zip file created")

from zipfile import*
f = ZipFile("D:/Rohit123/xyz.zip","r",ZIP_STORED)
names=f.namelist()
for name in names:
    print(name)
    f1 = open(name,'r')
    print(f1.read())