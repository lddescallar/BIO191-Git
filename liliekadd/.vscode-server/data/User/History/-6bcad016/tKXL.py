userInput = int(input("Please input side length of diamond: "))
n = userInput

for idx in range(n-1):
    print((n-idx) * ' ' + (2*idx+1) * '*')
for idx in range(n-1, -1, -1):
    print((n-idx) * ' ' + (2*idx+1) * '*')