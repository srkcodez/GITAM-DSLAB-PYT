# binary search function

def binarysearch(ele, piv):  # first argument list of elements, second argument pivot
    low = 0
    high = len(ele)
    while low <= high:  # we have to check equal condition too.
        mid = (low + high) // 2  # finds the mid position
        if piv == ele[mid]:  # return the position if the element is present at mid
            return mid
        elif piv < ele[mid]:  # search in the lower half by making high to mid-1
            high = mid - 1
        else:  # search in the upper half by making low to mid + 1
            low = mid + 1

    return -1  # if all the elements were searched return negative that represent element not found


# reading number of elements

n = int(input('enter number of elements'))

# reading elements in the list

element_list = []

for i in range(n):
    element_list.append(int(input('enter element')))

# sort the element list

element_list.sort()

# reading pivot element

pivot = int(input('enter element to search'))
# function call

res = binarysearch(element_list, pivot)  # returns index of the element if element present in the list otherwise -1

# we haven't print the resultant index

if res != -1:
    print('element is present at ', res + 1)  # to display the position of element
else:
    print('element is not found')

# run again

# let us check with one more input
# we did not get the result because array is not in sorted order

# to see that this mistake not happen sort the array after reading by using sort function


# that is all have a great day
# like share subscribe !!!!!
