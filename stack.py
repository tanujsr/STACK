"""stack = []
stack.append('a')
stack.append('b')
stack.append('c')
print("initial stack")
print(stack)
print(stack.__sizeof__())

print("\n elements poped from stack are:")
print(stack.pop())
print(stack.pop())
print(stack.pop())
print("elements after poped up are:-")
print(stack)

from collections import deque

stack = deque()
stack.append('a')
stack.append('b')
stack.append('c')
print("initial stack")
print(stack)
print("elements poped from stack are:-")
print(stack.pop())
print(stack.pop())
print(stack.pop())
print("elements after pop are:-")
print(stack)

from queue import LifoQueue

stack = LifoQueue(maxsize=5)
print(stack.qsize())
stack.put('a')
stack.put('b')
stack.put('z')
print("Full: ", stack.full())
print("Size: ", stack.qsize())
print("elements poped from stack are:-")
print(stack.get())
print(stack.get())
print(stack.get())
print(stack)


# Python3 program for array implementation of queue

# Class Queue to represent a queue
class Queue:

    # __init__ function
    def __init__(self, capacity):
        self.front = self.size = 0
        self.rear = capacity - 1
        self.Q = [None] * capacity
        self.capacity = capacity

    # Queue is full when size becomes
    # equal to the capacity
    def isFull(self):
        return self.size == self.capacity

    # Queue is empty when size is 0
    def isEmpty(self):
        return self.size == 0

    # Function to add an item to the queue.
    # It changes rear and size
    def EnQueue(self, item):
        if self.isFull():
            print("Full")
            return
        self.rear = (self.rear + 1) % (self.capacity)
        self.Q[self.rear] = item
        self.size = self.size + 1
        print("% s enqueued to queue" % str(item))

    # Function to remove an item from queue.
    # It changes front and size
    def DeQueue(self):
        if self.isEmpty():
            print("Empty")
            return

        print("% s dequeued from queue" % str(self.Q[self.front]))
        self.front = (self.front + 1) % (self.capacity)
        self.size = self.size - 1

    # Function to get front of queue
    def que_front(self):
        if self.isEmpty():
            print("Queue is empty")

        print("Front item is", self.Q[self.front])

    # Function to get rear of queue
    def que_rear(self):
        if self.isEmpty():
            print("Queue is empty")
        print("Rear item is", self.Q[self.rear])

    # Driver Code


if __name__ == '__main__':
    queue = Queue(30)
    queue.EnQueue(10)
    queue.EnQueue(20)
    queue.EnQueue(30)
    queue.EnQueue(40)
    queue.DeQueue()
    queue.que_front()
    queue.que_rear()

queue = []
queue.append(10)
queue.append(34)
queue.append(87)
queue.pop(0)
queue.insert(1,987)
print(queue)

queue = []
def enqueue():
    element = input("enter the element: ")
    queue.append(element)
    print(element,"is added to the queue!")
def dequeue():
    if not queue:
        print("queue is empty")
    else:
        e = queue.pop(0)
        print("removed element: ",e)
def display():
    print(queue)

while True:
    print("select the operation 1.add \n 2.remove \n 3.show \n 4.quit")
    choice = int(input())
    if choice == 1:
        enqueue()
    elif choice == 2:
        dequeue()
    elif choice == 3:
        display()
    elif choice ==4:
        exit()
    else:
        print("enter the correct operation!")


# Python Script to Implement two stacks in a list
class twoStacks:

    def __init__(self, n):  # constructor
        self.size = n
        self.arr = [None] * n
        self.top1 = -1
        self.top2 = self.size

    # Method to push an element x to stack1
    def push1(self, x):

        # There is at least one empty space for new element
        if self.top1 < self.top2 - 1:
            self.top1 = self.top1 + 1
            self.arr[self.top1] = x

        else:
            print("Stack Overflow ")
            exit(1)

        # Method to push an element x to stack2

    def push2(self, x):

        # There is at least one empty space for new element
        if self.top1 < self.top2 - 1:
            self.top2 = self.top2 - 1
            self.arr[self.top2] = x

        else:
            print("Stack Overflow ")
        exit(1)

    # Method to pop an element from first stack
    def pop1(self):
        if self.top1 >= 0:
            x = self.arr[self.top1]
            self.top1 = self.top1 - 1
            return x
        else:
            print("Stack Underflow ")
            exit(1)

        # Method to pop an element from second stack

    def pop2(self):
        if self.top2 < self.size:
            x = self.arr[self.top2]
            self.top2 = self.top2 + 1
            return x
        else:
            print("Stack Underflow ")
            exit()

        # Driver program to test twoStacks class


ts = twoStacks(5)
ts.push1(5)
ts.push2(10)
ts.push2(15)
ts.push1(11)
ts.push2(7)

print("Popped element from stack1 is " + str(ts.pop1()))
ts.push2(40)
print("Popped element from stack2 is " + str(ts.pop2()))


def stackcheck(expr):
    stack = []

    for char in expr:
        if char in ["(", "{", "["]:
            # Push the element in the stack
            stack.append(char)


        else:
            if not stack:
                return False
            current_char = stack.pop()
            if current_char == '(':
                if char != ")":
                    return False
            if current_char == '{':
                if char != "}":
                    return False
            if current_char == '[':
                if char != "]":
                    return False
            #check empty stack
        if stack:
            return False
        return True
    # Driver Code
    if __name__ == "__main__":
        expr = "{()}[]"

        # Function call
        if areBracketsBalanced(expr):
            print("Balanced")
        else:
            print("Not Balanced")"""

def reverse(string):
    string = string[::-1]
    return string

#print("enter a string")
string = input("enter a string\n")
string = reverse(string)
print("Reversed string is " + string)







