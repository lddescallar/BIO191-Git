userInput = int(input("Please input side length of diamond: "))

if userInput > 0:
    for i in range(userInput):
        for s in range(userInput -3, -2, -1):
            print(" ", end="")
        for j in range(i * 2 -1):
            print("*", end="")
        print()
    for i in range(userInput, -1, -1):
        for j in range(i * 2 -1):
            print("*", end="")
        print()