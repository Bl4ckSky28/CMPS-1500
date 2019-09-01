import time
import random
from BST import *



nlist = [100, 500, 1000, 5000, 10000, 20000, 30000, 40000, 50000]
for n in nlist:
    L = list(range(n))
    random.shuffle(L)
    
    # Construct a binary search tree from the elements in L
    # ADD CODE to measure runtime

bst = BST() # Empty BST
tstart = time.time()
for i in range(100): # Add all elements in L, one at a time
    bst.insert(L[i])
tend = time.time()
ttotal = tend - tstart

t = time.time()
for x in range(500):
    bst.find(random.choice(L))
t2 = time.time()
tfinal = t2 - t

print(ttotal)
print(tfinal)
    # ADD CODE to perform 500 find operations in bst (each time pick
    # a random element from L and then find it in bst)
    # ADD CODE to measure runtime 

