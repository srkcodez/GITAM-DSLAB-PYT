#recursion

def printnum(n):
    if n==1:
        return
    else:
        print(n)
        printnum(n-1)


def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)


printnum(25)
print(fact(5))