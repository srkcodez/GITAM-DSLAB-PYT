class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CSLL:

    def __init__(self):
        self.head = None

    def insertBegin(self, data):

    def insertEnd(self, data):


    def display(self):
        temp = self.head
        while temp.next is not self.head:
            print(temp.data, end="-->")
            temp = temp.next
        print(temp.data)



#driver code

l1 = CSLL()
ch = 1
l1.insertBegin(20)
l1.insertBegin(30)
ele = int(input('enter element to insert in the begin:'))
l1.insertBegin(ele)
l1.insertEnd(40)
l1.insertEnd(50)
ele = int(input('enter element to insert in the end:'))
l1.insertEnd(ele)
l1.display()
