

def removeSpaces(s):
    newS = ""
    for c in s:
        if c != " ":
            newS += c
    return newS

myString = "Hello world"
myString = removeSpaces(myString)
print(myString)

def removeSpaces2(L):
    newL = []
    for c in L:
        if c != " ":
            newL.append(c)
    return newL

myList = ['H', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
myList = removeSpaces2(myList)
print(myList)

class Person:
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName

    def __repr__(self):
        return self.firstName + ' ' + self.lastName

def toString(head):
    current = head
    myString = ""
    while current != None:
        myString += str(current.data) + '->'
        current = current.next
    return myString
        

        
        








    
    
