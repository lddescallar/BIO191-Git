seq = GCAGTTGCA
print(seq)
l = list(seq)
for i in range(len(seq)):
    if seq[i] == 'G':
        l[i] = 'C' #assign the complement in the list
    if seq[i] == 'C':
        l[i] = 'G' #assign the complement in the list
    if seq[i] == 'A':
        l[i] = 'T' #assign the complement in the list
    if seq[i] == 'T':
        l[i] = 'A' #assign the complement in the list

seq = "".join(l)  #copy the list back to seq

print(seq[::-1])