N = int(input("Enter an integer:"))

for i in range (0,N+2):
    for j in range (0,N+2):
        if (j == N-1 or i == 3):
            print("*",end="")