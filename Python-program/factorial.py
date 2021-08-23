num = int(input("Enter number: "))
i = 1
factorial = 1
while i<=num:
    factorial = factorial * i
    i = i + 1
print("Factorial of",num,"is",factorial)