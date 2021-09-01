f = open('abc.txt','r')
print("name:",f.name)
print("mode:",f.mode)
print("closed:",f.closed)
print("is readable:",f.readable())
print("is writable:",f.writable())
f.close()
print("closed:",f.closed)

#write data

f =open('abc.txt','w')
f.write("java\n")
f.write("programming\n")
f.write("lang\n")
print("write data successfully")
f.close()

#write list
f = open("abc.txt","w")
list = ["c\n","c++\n","java\n","python\n","sql\n","data science\n"]
f.writelines(list)
print("list of lines write successfully")
f.close()

#read total data
f = open("abc.txt","r")
data = f.read()
print(data)
f.close()

#read 10 char
f = open("abc.txt","r")
data1=f.read(10)
print(data1)
f.close()

#read line by line

f = open("abc.txt","r")
line1 = f.readline()
print(line1,end="")
line2 = f.readline()
print(line2,end="")
line3 = f.readline()
print(line3,end="")
line4 = f.readline()
print(line4,end="")

#read all lines into list
f = open("abc.txt","r")
lines = f.readlines()
for line in lines:
    print(line,end="")
f.close()