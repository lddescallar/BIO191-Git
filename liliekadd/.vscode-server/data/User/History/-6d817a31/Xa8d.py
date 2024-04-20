x = int(input("Please enter an integer:"))
y = int(input("Please enter another integer:"))
z = int(input("Please enter a third integer:"))

maxOddNum = x
if y > maxOddNum and y % 2 != 0:
    maxOddNum = y
if z > maxOddNum and z % 2 != 0:
    maxOddNum = z
if x = maxOddNum and x % 2 != 0:
    maxOddNum = x
print(maxOddNum, "is the greatest")