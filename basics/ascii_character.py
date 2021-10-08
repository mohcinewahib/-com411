print("Program Started")
i = int (input("Please enter an ASCII code: "))
print(i)
if i in range( 32,126 ):
    print("The character represented by the ASCII code " + str(i) + "is ", chr(i))
else:
    print("ERROR")
print("Program Ended")