class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CSLL:

    def __init__(self):
        self.head = None

    def insertBegin(self, data):
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
            newnode.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            newnode.next = self.head
            temp.next = newnode
            self.head = newnode

    def insertEnd(self, data):
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
            newnode.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            newnode.next = self.head
            temp.next = newnode

    def deleteEnd(self):
        if self.head is None:
            print('no elements present')
        else:
            temp = self.head
            while temp.next.next != self.head:
                temp = temp.next
            #print(temp.next.data, 'deleted successfully')
            temp.next = self.head

    def deleteBegin(self):
        if self.head is None:
            print('no elements present')
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            #print(self.head.data, 'deleted successfully')
            temp.next = self.head.next
            self.head = self.head.next

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
l1.deleteEnd()
l1.insertBegin(30)
ele = int(input( ))
l1.insertBegin(ele)
l1.deleteBegin()
l1.insertEnd(40)
l1.deleteEnd()
l1.insertEnd(50)
ele = int(input( ))
l1.insertEnd(ele)
l1.display()
