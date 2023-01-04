class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class CDLL:

    def __init__(self):
        self.head = None

    def insertBegin(self, data):
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
            newnode.next = self.head
            newnode.prev = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            newnode.next = self.head
            newnode.prev = temp
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
            newnode.prev=temp
            newnode.next = self.head
            temp.next = newnode

    def deleteEnd(self):
        if self.head is None:
            print('no elements present')
        elif self.head.next is self.head:
            self.head = None
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            print(temp.data,'deleted successfully')
            temp.prev.next=self.head
            self.head.prev=temp

    def deleteBegin(self):
        if self.head is None:
            print('no elements present')
        elif self.head.next is self.head:
            self.head = None
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            print(self.head.data,'deleted successfully')
            self.head = self.head.next
            temp.prev.next=self.head
            self.head.prev=temp.prev




    def display(self):
        temp = self.head
        while temp.next is not self.head:
            print(temp.data, end="-->")
            temp = temp.next
        print(temp.data)


l1 = CDLL()
l1.insertBegin(10)
l1.display()
l1.insertBegin(20)
l1.display()
l1.insertBegin(30)
l1.display()
l1.insertEnd(40)
l1.display()
l1.deleteEnd()
l1.display()
l1.deleteBegin()
l1.display()
