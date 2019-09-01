
p = input("Please enter a password (press [enter] to finish): ")
list = []
list.append(p)

while p != '':
    p = input("Please enter a password (press [enter] to finish): ")
    list.append(p)
    
print(list[:-1])

stars = []
for x in list:
    length = len(x)
    tempStr = '*' * length
    stars.append(tempStr)
    
print(stars[:-1])
        
