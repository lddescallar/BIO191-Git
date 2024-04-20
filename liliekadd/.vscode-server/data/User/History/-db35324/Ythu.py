N = int(input("Enter N: "))
print (N)

if N%2==1 and N>0:
    for i in range(N):
        for j in range(N):
             if i == j :
                print("*", end="")
             elif i == N//2:
                print("*", end="")
             elif j == N//2:
                print("*", end="")
             elif j+1 == N-i:
                print("*", end="")
             else:
                print(" ", end="")
        print("")