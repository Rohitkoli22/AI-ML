#write dat to csv file

import csv
import zipfile
with open("D:\Rohit123/emp.csv","w",newline="") as f:
    w =csv.writer(f)
    w.writerow(["END","ENAME","ESAL","EADDR"])
    n = int(input('Enter Number of employee: '))
    for i in range(n):
        eno = input("Enter Employee no: ")
        ename = input("Enter Employee Name: ")
        esal = input("Enter Employee salary: ")
        eaddr = input("Enter Employee Address: ")
        w.writerow([eno,ename,esal,eaddr])
    print("successfull")


#read data
file = open("D:\Rohit123/emp.csv","r")
a = csv.reader(file)
data = list(a)
for line in data:
    for word in line:
        print(word,"\t",end="")
    print()





