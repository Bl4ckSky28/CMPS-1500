

from Node import *

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        
    def enqueue(self, item):
        if self.tail != None:
            self.tail.next = Node(item)
            self.tail = self.tail.next
        else:
            self.head = Node(item)
            self.tail = self.head
        self.size += 1
        
    def dequeue(self):
        if self.head != None:
            current = self.head
            self.head = self.head.next
            self.size -= 1
            return current.data
        else:
            return None

    def isEmpty(self):
        return self.size == 0

    def __repr__(self):
        string = 'head-> '
        current = self.head
        while current != None:
            string += str(current.data) + ' '
            current = current.next
        string += ' <-tail'
        return string
        

        

