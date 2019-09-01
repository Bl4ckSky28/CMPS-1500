
password = input("Please enter a password:\n")

number_exists = False
letter_exists = False
special_exists = False
space_notexists = True

numbers = '0123456789'
letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
special = '!?,.;:$#_&'
bad = ' '
length = len(password)

while True:
    for c in password:
        if c in numbers:
            number_exists = True
        if c in letters:
            letter_exists = True
        if c in special:
            special_exists = True
        if c in bad:
            space_notexists = False
    if number_exists and letter_exists and special_exists and length >= 8 and length <= 20 and space_notexists:
        print('Password accepted')
        break
    else:
        password = input("Please enter a password:\n")
        length = len(password)
        


        

        
        
