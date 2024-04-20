top = int(input("Please enter the numerator:"))
bottom = int(input("Please enter the denominator:"))
if bottom != 0 and top % bottom == 0:
print("The numerator is evenly divided by the denominator.")
else:
print("The fraction is not a whole number.")