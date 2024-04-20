x = int(input("Please enter an integer:"))
y = int(input("Please enter another integer:"))
z = int(input("Please enter a third integer:"))

maxOddNum = x
Odd = True
if y > maxOddNum and y % 2 != 0:
    maxOddNum = y
if z > maxOddNum and z % 2 != 0:
    maxOddNum = z
if x % 2 != 0:
    Odd = False
if Odd:
    print(maxOddNum, "is the greatest odd integer")
else:
    print("All integers are even numbers.")