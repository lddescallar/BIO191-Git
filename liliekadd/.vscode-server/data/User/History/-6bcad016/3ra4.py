N = int(input("Please input side length of diamond: "))

if N > 0:
    for i in range(N):
        for s in range(N -3, -2, -1):
            print(" ", end="")
        for j in range(i * 2 -1):
            print("*", end="")
        print()
    for i in range(N, -1, -1):
        for j in range(i * 2 -1):
            print("*", end="")
        print()