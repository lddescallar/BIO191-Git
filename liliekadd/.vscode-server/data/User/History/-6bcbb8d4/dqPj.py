N= 10
for row in range(1,N):
    print(*("{:3}".format(row*col) for col in range(1, N)))