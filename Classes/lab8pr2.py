
from Node import *

def toStringRec(head):
    current = head
    if current == None:
        return str(current)
    else:
        return toStringRec(current.next)

def findElement(head, i):
    current = head.root
    while current:
        if current.data == i:
            return 
    return current
    return "None"
