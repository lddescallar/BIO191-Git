N = int(input("Enter an integer:"))

for i in range (0,2*N-1):
    for j in range (0,2*N-1):
        if (j == N-1):
            print("*",end="")
        elif (i + 2 == j - 1):
            print("*",end="")
        else:
            print(" ",end="")
    print("")