def main():

    rows = 10
    counter = 0
    multiplicationTable(rows,counter)

def multiplicationTable(rows,counter):

    size = rows + 1

    for i in range (1,size):
        for nums in range (1,size):
            value = i*nums
            print(value,sep=' ',end="\t")
            counter += 1
            if counter%rows == 0:
                print()
            else:
                counter
main()