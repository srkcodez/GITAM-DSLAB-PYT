l1 = []
for i in range(5):
    l1.append(int(input()))

for i in range(5):
    min = l1[i]
    minpos=i
    for j in range(i+1,5):
        if l1[j] < min:
            min=l1[j]
            minpos=j
    l1[i],l1[minpos]=l1[minpos],l1[i]

for i in range(5):
    print(l1[i], end=" ")
