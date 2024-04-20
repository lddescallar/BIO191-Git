size = int(input("Enter an integer:"))

for i in range (0,size):
    for j in range (0,2*size+1):
        if (j==0 or j==size-1 or j>size):
            print("*",end="")
        elif ((i==0 or i==size-1) and j!=size):
            print("*",end="")
        else:
            print(" ",end="")
    print("")