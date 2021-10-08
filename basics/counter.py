even = 0
odd = 0
x = int(input("enter first number; "))
y = int(input("enter second number; "))
z = int(input("enter third number; "))
group = (x, y, z)
for i in group:
    if (i % 2) == 0:
        even = even + 1
    else:
        odd = odd + 1;
print(f"there are {even} even numbers and {odd} odd numbers")

