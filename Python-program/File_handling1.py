import os,sys
num_lines= 0
num_char = 0
fname = input("Enter file name: ")
if os.path.isfile(fname):
    print("File Exists:",fname)
    with open(fname,'r') as f:
        for line in f:
            num_lines = num_lines + 1
            str = line.split()
            str1 = ''.join(str)
            num_char = num_char + len(str1)
    print("Number of lines in file: ", num_lines)
    print("Number of character in file: ",num_char)
    f = open(fname,"r")
    print("\n\nthe content of file is:")
    data = f.read()
    print(data)

else:
    print("File doesnot exists:",fname)