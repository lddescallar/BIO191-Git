x = int(input("Please enter an integer:"))
y = int(input("Please enter another integer:"))
z = int(input("Please enter a third integer:"))
# Here is our initial guess
maxNum = x
if y > maxNum: # Fix our guess if needed
    maxNum = y
if z > maxNum: # Fix our guess again if needed
    maxNum = z
print(maxNum,"is greatest.")
print("Done.")