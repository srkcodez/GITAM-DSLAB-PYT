# stack is a linear data structure in which insertion and deletion performed at one end called top end
# insertion operation is called as push
# deletion operation is called as pop
# top -> it is the pointer points to the top of the element
# basepointer (bp) --> points to the begining of the stack
# max size is the maximum number of elements that can be stored in the stack
# overflow means if the number of elements exceeds the maximum size then it is called as overflow
# underflow means if there are no elements present in the stack means underflow

# class definition for stack

class Stack:

    def __init__(self, max):
        self.data = []  # to store the data items
        self.top = -1  # to point to the top element
        self.max = max  # to define the maximum size

    # push operation

    def push(self, ele):

        # after insertion top pointer will we incremented by 1 if we reach to the maximum size we can not insert more elements
        # hence we are verifying the overflow condition before insertion
        if self.top + 1 >= self.max:
            print("overflow")
        # if it is not overflow then increment top pointer and insert the element
        else:
            self.top = self.top + 1
            self.data.insert(self.top, ele)
            print(ele,"inserted successfully")
    def pop(self):
        if (self.top < 0):
            print("underflow")
        else:
            print(self.data[self.top],"deleted successfully")
            self.top -= 1
            self.data.pop()

    def display(self):
        if self.top < 0 :
            print("underflow")
        else:
            print("elements in stack are")
            for i in range(self.top,-1,-1):
                print(self.data[i])
            print()



# driver code:
#object of stack
s1=Stack(10) #creating a stack object with maximum size 10
ch=5
while ch!=4:
    ch=int(input('\n 1. push element \n 2. pop element \n 3. display elment \n 4. exit'))
    if ch==1:
        ele=int (input('eneter element to be inserted'))
        s1.push(ele)
    elif ch==2:
        s1.pop()
    elif ch==3:
        s1.display()
    elif ch==4:
        exit(0)
    else:
        print('invalid choice')


# Thank you Like share and subscribe