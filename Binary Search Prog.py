def binarysearch(ele, piv):
    low = 0
    high = len(ele)
    while low <= high:
        mid = (low + high) // 2
        if piv == ele[mid]:
            return mid
        elif piv < ele[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1