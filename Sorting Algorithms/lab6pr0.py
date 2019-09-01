
def is_sorted(lst):
    i = 1
    while i < len(lst):
        if lst[i] < lst[i - 1]:
            return False
        i += 1
    return True
    
#test_list0 = [1, 2, 3, 4, 5]
#test_list1 = [5, 4, 2, 4, 2]
#test_list2 = [1, 2, 2, 3, 3, 5]
#test_list3 = [5, 4, 4, 2, 6]

def is_file_sorted(filename):
    file = open(filename)
    list = []
    #initiates a loop that iterates over every line in file
    for line in file:
        #adds lines from file to the list and converts them to an integer
        list.append(int(line))
    if is_sorted(list):
        return True
    return False

