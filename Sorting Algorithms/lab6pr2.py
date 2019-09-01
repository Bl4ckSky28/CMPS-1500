

def selection_sort(aList):
  """Sorts a list in ascending order using the selection sort algorithm.
  """
  n = len(aList)
  for i in range(n-1):
    
      
    # Find the minimum element in the unsorted portion of the list
    
    smallNdx = i # assume the ith element is the smallest.
    
    # Determine if any other element contains a smaller value.
    for j in range(i+1, n):
      if aList[j] < aList[smallNdx]:
        smallNdx = j

    # Swap the ith value and smallNdx value  
                      
    tmp = aList[i]
    aList[i] = aList[smallNdx]
    aList[smallNdx] = tmp

  return aList  

def merge(left, right):
    """
    Merge to sorted list, left and right, into one sorted list.
    """
    aList = []
    lt = 0
    rt = 0

    # Repeatedly move the smallest of left and right to the new list
    while lt < len(left) and rt < len(right):
        if left[lt] < right[rt]:
            aList.append(left[lt])
            lt += 1
        else:
            aList.append(right[rt])
            rt += 1

    # There will only be elements left in one of the original two lists.

    # Append the remains of left (lt..end) on to the new list.
    while lt < len(left):
        aList.append(left[lt])
        lt += 1
         
    # Append the remains of right (rt..end) on to the new list.
    while rt < len(right):
        aList.append(right[rt])
        rt += 1

    return aList

def merge_sort(aList):
    """
    Merge sort recursively divides the list into half, sorts both halves
    and then merges the two sorted lists into one.
    """
    # If the aList is size 0 or 1, it's already sorted.
    if len(aList) <= 1:
        return aList

    else:
        mid = len(aList) // 2

        # Recursively sort each half
        left = merge_sort(aList[:mid]) # left half, L[0..n/2-1]
        right = merge_sort(aList[mid:]) # right half, L[n/2..n-1]
        
        # Merge the two (each sorted) parts back together
        return merge(left, right)

def use_mergesort(inputfile, outputfile):
    list = []
    file = open(inputfile, 'r')
    
    for line in file:
        list.append(int(line))
        
    f = open(outputfile, 'w')
    list = merge_sort(list)
    
    for item in list:
        f.write(str(item))
        f.write('\n')
        
    f.close()
    
def use_selectionsort(inputfile, outputfile):
    list = []
    file = open(inputfile, 'r')

    for line in file:
        list.append(int(line))

    f = open(outputfile, 'w')
    list = selection_sort(list)

    for item in list:
        f.write(str(item))
        f.write('\n')
    f.close()

import random
random.seed(0)

#generates a file with n random integers
def generate_nums(filename, n):
    file = open(filename, 'w')
    for num in range(n):
        file.write(str(random.randrange(0, 100)))
        file.write('\n')
    file.close()
    
