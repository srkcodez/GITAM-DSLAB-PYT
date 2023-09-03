l1 = []
for i in range(5):
    l1.append(int(input()))
for i in range(5):
    for j in range(5 - i - 1):
        if l1[j] > l1[j + 1]:
            l1[j], l1[j + 1] = l1[j + 1], l1[j]
for i in range(5):
    print(l1[i],end=" ")
