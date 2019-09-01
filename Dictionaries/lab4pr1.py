
def look_up(d):
    name = input("Enter a name: ")
    if name in d:
        print (d[name])
    else:
        print('Not found.')

def add(d):
    name = input("Enter a name: ")
    major = input("Enter a major: ")
    if name in d:
        print("A person with this name already exists in the system.")
    else:
        d[name] = major

def change(d):
    name = input("Enter a name: ")
    if name in d:
        major = input("Enter the new major: ")
        d[name] = major
    else:
        print("That name is not found.")

def delete(d):
    name = input("Enter a name: ")
    if name in d:
        del d[name]
    else:
        print("That name is not found.")

def display(d):
    for i,j in d.items():
        print("{} is a wizard in {}".format(i,j))

def get_menu_choice():
        print("""Majors of College Students
        ---------------------------
        1. Look up a student’s major
        2. Add a new student
        3. Change a major
        4. Delete a student
        5. Display all students
        6. Quit the program""")

        letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        correct = True
        choice = input("Enter your choice: ")
        
        if len(choice) != 1 or int(choice) < 1 or int(choice) > 6:
            correct = False
        while correct == False:
            choice = input("Enter a valid choice: ")
            if len(choice) != 1 or choice in letters:
                choice = input("Enter a valid choice: ")
            else:
                choice = int(choice)
                return choice
                break
        choice = int(choice)
        return choice

majors = {}
choice = 0
myFile = open('dictionary.txt', 'w')

while choice != 6:
        choice = get_menu_choice()
        if choice == 1:
            look_up(majors)
        elif choice == 2:
            add(majors)
        elif choice == 3:
            change(majors)
        elif choice == 4:
            delete(majors)
        elif choice == 5:
            display(majors)
            
#writes final major list to file
myFile.write(str(majors))
#closes file
myFile.close()
#opens file dictionary.txt for reading
myFile = open('dictionary.txt', 'r')
#reads contents of file
print(myFile.read())



