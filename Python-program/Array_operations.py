from array import*
a = array('i',[10,20,30,40,50])
print(a)
#insert or append value into array
a.append(60)
print(a)
a.insert(3,70)
print(a)
#pop or remove element in array
print(a.pop())
print(a.pop(3))
print(a)
a.remove(10)
print(a)
#extend
a.extend([80,90,100])
print(a)

b = array('i',[15,25,35,45,55])
c = array('i')
c= a+b
print("array c = ",c)
#slicing
print(a[0:5])
