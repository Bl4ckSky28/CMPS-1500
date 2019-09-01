
def is_sorted(lst):
    i = 1 # O(1)
    while i < len(lst): # O(N)
        if lst[i] < lst[i - 1]: # O(N^2)
            return False # O(1)
        i += 1 # O(N)
    return True # O(1)

def is_file_sorted(filename):
    file = open(filename) # O(1)
    list = [] # O(1)
    for line in file: # O(N)
        list.append(int(line)) # O(1)
    if is_sorted(list): # O(1)
        return True # O(1)
    return False # O(1)

userInput = input("Please enter a filename: ") # O(1)

if is_file_sorted(userInput): # O(1)
    print("Congratulations! The file", userInput, "is nicely sorted!") # O(1)
else: # O(1)
    print("Looks like", userInput, "needs to be sorted") #O(1)

#total big-O run time is O(N^2) because it is the largest estimation of N
    
