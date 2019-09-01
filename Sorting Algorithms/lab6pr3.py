"""Name: Grayson Buchholz and Dylan Rothstein
    Course: CMPS 1500
    Lab Section: Thursday 3:30-4:45 pm
    Assignment: Lab 6 Part 3
    Date: 03/21/2019
"""

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
    
def analyze_mergesort(inputfile, outputfile):
    #imports time library
    import time
    
    #start time total and inputs
    totalTimeStart = time.time()
    readTimeStart = time.time()
    
    list = []
    file = open(inputfile, 'r')
    for line in file:
        list.append(int(line))
        
    #end time for inputs
    readTimeEnd = time.time()
    
    f = open(outputfile, 'w')
    
    #start time for sorting
    sortTimeStart = time.time()
    
    list = merge_sort(list)
    
    #end time for sorting
    sortTimeEnd = time.time()
    #start time for outputs
    outputTimeStart = time.time()
    
    for item in list:  
        f.write(str(item)) 
        f.write('\n')
    f.close()
    
    #end time for outputs 
    outputTimeEnd = time.time()
    #end time for total run time
    totalTimeEnd = time.time()
    #number of values processed
    valuesProcessed = len(list)

    #print statements in correct format
    print("It took", round(readTimeEnd - readTimeStart, 6), "seconds to input", valuesProcessed, 'values', "from file", inputfile)
    print("It took", round(sortTimeEnd - sortTimeStart, 6), "seconds to sort", valuesProcessed, 'values', "using merge sort")
    print("It took", round(outputTimeEnd - outputTimeStart, 6), "seconds to output", valuesProcessed, 'values', "to file", outputfile)
    print("Total time the program took is", round(totalTimeEnd - totalTimeStart, 6))
    
def analyze_selectionsort(inputfile, outputfile):
    #imports time library
    import time
    
    #start time for total run time and inputs
    totalTimeStart = time.time()
    readTimeStart = time.time()
    
    list = []
    file = open(inputfile, 'r')
    for line in file:
        list.append(int(line))

    #end time for inputs
    readTimeEnd = time.time()
    
    f = open(outputfile, 'w')
    
    #start time for sorting
    sortTimeStart = time.time()
    
    list = selection_sort(list)

    #end time for sorting
    sortTimeEnd = time.time()
    #start time for outputs
    outputTimeStart = time.time()
    
    for item in list:
        f.write(str(item))
        f.write('\n')
    f.close()

    #end time for outputs
    outputTimeEnd = time.time()
    #end time for total run time
    totalTimeEnd = time.time()
    #number of values processed
    valuesProcessed = len(list)

    #print statements in correct format
    print("It took", round(readTimeEnd - readTimeStart, 6), "seconds to input", valuesProcessed, 'values', "from file", inputfile)
    print("It took", round(sortTimeEnd - sortTimeStart, 6), "seconds to sort", valuesProcessed, 'values', "using selection sort")
    print("It took", round(outputTimeEnd - outputTimeStart, 6), "seconds to output", valuesProcessed, 'values', "to file", outputfile)
    print("Total time the program took is", round(totalTimeEnd - totalTimeStart, 6))

def generate_nums(filename, n):
    import random
    random.seed(0)
    file = open(filename, 'w')
    for num in range(n):      
        file.write(str(random.randrange(0, 100)))
        file.write('\n')
    file.close()

#generate files with numbers to be sorted
generate_nums("ten.txt", 10)
generate_nums("hundred.txt", 100)
generate_nums("thousand.txt", 1000)
generate_nums("tenthousand.txt", 10000)
generate_nums("hundredthousand.txt", 100000)
generate_nums("million.txt", 1000000)

#implements algorithum analysis 
analyze_mergesort("ten.txt", "ten.txt")
analyze_mergesort("hundred.txt", "hundred.txt")
analyze_mergesort("thousand.txt", "thousand.txt")
analyze_mergesort("tenthousand.txt", "tenthousand.txt")
analyze_mergesort("hundredthousand.txt", "hundredthousand.txt")
analyze_mergesort("million.txt", "million.txt")

#generate files with numbers to be sorted
generate_nums("ten.txt", 10)
generate_nums("hundred.txt", 100)
generate_nums("thousand.txt", 1000)
generate_nums("tenthousand.txt", 10000)
generate_nums("hundredthousand.txt", 100000)
generate_nums("million.txt", 1000000)

#implements algorithum analysis 
analyze_selectionsort("ten.txt", "ten.txt")
analyze_selectionsort("hundred.txt", "hundred.txt")
analyze_selectionsort("thousand.txt", "thousand.txt")
analyze_selectionsort("tenthousand.txt", "tenthousand.txt")
analyze_selectionsort("hundredthousand.txt", "hundredthousand.txt")
analyze_selectionsort("million.txt", "million.txt")



