print("Program Started")
v = input("Please enter a standard character: ")
length = len(v)
if length == 1:
    print("The ASCII code for" + v + "is ", ord(v))
else:
    print("ERROR")
print("Program Ended")