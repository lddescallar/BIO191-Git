age = int(input("What is your age?:"))
ownlicense = int(input("Do you have a fishing license in MN (yes/no)?:"))
parentlicense = int(input("Does your parent have a fishing license (yes/no)?:"))

if age <= 15 and ownlicense == 'yes' or 'no' and parentlicense == 'yes':
    print("You are legal to fish in MN.")
else:
    print("You are not legal to fish in MN.")
