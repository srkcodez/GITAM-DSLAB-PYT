def LinearSearch(ele, p):
    for j in range(len(ele)):
        if ele[j] == p:
            return j
    return -1


elements = []
n = int(input('enter n value'))

for i in range(n):
    elements.append(int(input('enter value%d' % (i + 1))))

pivot = int(input('enter the element to search'))

result = LinearSearch(elements, pivot)

if result == -1:
    print('element not found')
else:
    print('element is present at %d' % (result + 1))
