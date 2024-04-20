dimensions = int(input(">"))
for row_1 in range (dimensions):
    for col_1 in range (dimensions):
        print (("*"), end="")
    print()

inner_dimensions = dimensions - 2
print ('*' * dimensions)
for i in range(inner_dimensions):
    print ('*' + ' ' * inner_dimensions + '*')
print ('*' * dimensions)