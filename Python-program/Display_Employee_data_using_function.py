def showEmployee(name,salary=9000):
    print("Employee Name: ",name)
    print("Salary: ",salary)
name=""
salary=0
showEmployee(name=input("Enter name: "),salary=int(input("Enter Salary: ")))
showEmployee(name=input("Enter name: "))