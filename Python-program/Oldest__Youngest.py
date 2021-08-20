man1_age = int(input("Enter age of man1: "))
man2_age = int(input("Enter age of man2: "))
man3_age = int(input("Enter age of man3: "))

d= {man1_age:"Man 1", man2_age:"Man 2", man3_age:"Man 3"}

younger = min(d)

print(str(d[younger])+ " is Yongest with age = " + str(younger))

oldest = max(d)

print(str(d[oldest])+ " is Oldest with age = " + str(oldest))

