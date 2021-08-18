#logical And
a = 10
b = 8
c = -5
d =  0
result = a>b and b>c and c<d
print("result=",result)

result1 = a>b and b>c and c>d
print("result1=",result1)

#logical or
a = 10
b = 8
c = -5
d =  0

result_1 = a>b or b<c or c<d
print("result_1=",result_1)

result_2 = a<b or b<c or c>d
print("result_2",result_2)

result_3 = a<b or b<c or c<d
print("result_3",result_3)
#logical Not
x = True
print(not x)
y = False
print(not y)
