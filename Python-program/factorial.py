num = int(input("Enter number: "))
i = 2
factorial = 1
while i<=num:
    factorial = factorial * i
    i = i + 1
print("Factorial of",num,"is",factorial)