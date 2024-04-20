row = 3
column = 5

for i in range(0, column):
    for j in range(0,row):
        if j % 2 == 0:
            print ("_")
        if j % 2 != 0:
            print ("*")