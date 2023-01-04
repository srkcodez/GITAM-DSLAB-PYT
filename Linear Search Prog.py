

# Linear Search
def LinearSearch(ele,pivot):
    for i in range(len(ele)):
        if ele[i]==pivot:
            return i+1
    return -1


#read the number of elements

n=int(input('enter number of elements:'))
ele=[]
for i in range(n):
    ele.append(int(input('enter element')))
pivot=int(input('enter pivot element'))


result=LinearSearch(ele,pivot)

if result != -1:
    print("element found at location %d"%result)
else:
    print("element is not present")



