class CircularQueue:
    # constructor
    def __init__(self, size):  # initializing the class
        self.size = size
        # initializing queue with none
        self.queue = [0 for i in range(size)]
        self.front = 0
        self.rear = -1

    def enqueue(self, data):
        # condition if queue is full
        if (self.rear + 1) % self.size == self.front:
            print(" Queue is Full\n")
        # condition for empty queue
        else:
            # next position of rear
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = data

    def dequeue(self):
        if self.front == -1:  # condition for empty queue
            print("Queue is Empty\n")
        # condition for only one element
        else:
            temp = self.queue[self.front]
            self.front = (self.front + 1) % self.size
            return temp

    def display(self):
        # condition for empty queue
        if self.front == -1:
            print("Queue is Empty")
        elif self.rear >= self.front:
            print("Elements in the circular queue are:",
                  end=" ")
            for i in range(self.front, self.rear + 1):
                print(self.queue[i], end=" ")
            print()
        else:
            print("Elements in Circular Queue are:",
                  end=" ")
            for i in range(self.front, self.size):
                print(self.queue[i], end=" ")
            for i in range(0, self.rear + 1):
                print(self.queue[i], end=" ")
            print()


# Driver Code
ob = CircularQueue(5)
ch = 1
while ch != 4:
    ch = int(input("Enter 1 to enqueue,2 to dequeue,3 to display 4 to exit"))
    if ch == 1:
        ele = input('enter element to input')
        ob.enqueue(ele)
    elif ch == 2:
        print('deleted element is: ', ob.dequeue())
    elif ch == 3:
        ob.display()
