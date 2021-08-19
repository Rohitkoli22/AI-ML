#bitwise and
a = 20
b = 4
print(a & b)

#bitwise or
a = 20
b = 4
print(a | b)

#bitwise x-or
a = 20
b = 4
print(a ^ b)
#one's compliment
a = 90
print(~a)

a = -50
print(~a)

#Left Shift
a = 13
b = 4
print(a<<b)

#Right Shift
a = 15
b = 3
print(a>>b)

#in
list = [1,5,4,7,9,15,30,89]
x = 15
print(x in list)

#not in
print(x not in list)

str = "Captain Jack Sparrow"
print("Jack" in str)

#identity
a = 47
b = 47
print(a is b)
x = 50
y = "50"
print(x is y)
print(x is not y)