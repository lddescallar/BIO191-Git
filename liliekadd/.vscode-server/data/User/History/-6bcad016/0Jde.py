userInput = int(input("Please input side length of diamond: "))
if userInput > 0:             
    for i in range(userInput):
        for s in range (userInput - i) :
            print(" ", end="")
        for j in range((i * 2) - 1):
            print("*", end="")
        print()
    for i in range(userInput, 0, -1):
        for s in range (userInput - i) :
            print(" ", end="")
        for j in range((i * 2) - 1):
            print("*", end="")
        print()