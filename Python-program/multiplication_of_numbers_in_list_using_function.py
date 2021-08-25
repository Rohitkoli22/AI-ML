def multiplication(numbers):
    total=1
    for item in numbers:
        total *= item
    return total
print("Total= ",multiplication((5,6,8,3,9)))