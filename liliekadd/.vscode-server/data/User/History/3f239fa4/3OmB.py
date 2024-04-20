N = int(input("Enter an integer:"))

for i in range (0,2*N-1):
    for j in range (0,2*N-1):
        if (j == N-1 or i == N-1):
            print("*",end="")
        if ((i== N or i == N/2) and j!=0 and j!=2*N-2):
            print("*",end="")
        else:
            print(" ",end="")
    print("")