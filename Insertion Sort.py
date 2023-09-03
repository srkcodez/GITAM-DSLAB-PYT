l1 = []
for i in range(5):
    l1.append(int(input()))

for i in range(1, 5):
    j = i
    while j > 0 and l1[j] < l1[j - 1]:
        l1[j], l1[j - 1] = l1[j - 1], l1[j]
        j -= 1

for i in range(5):
    print(l1[i], end=" ")
