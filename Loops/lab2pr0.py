
phrase = input("Please enter a phrase: ")
counter = 0
password = ''
password += phrase[0]

while counter < len(phrase):
    if phrase[counter] == '.':
        password += '.'
    elif phrase[counter] == ',':
        password += ','
    elif phrase[counter] == '?':
        password += '?'
    elif phrase[counter] == ';':
        password += ';'
    elif phrase[counter] == ':':
        password += ':'
    elif phrase[counter] == ' ':
        password += phrase[counter + 1]
    counter += 1

newPassword = ''

for c in password:
    if c in 'o':
        newPassword += '0'
    elif c in 'a':
        newPassword += '@'
    elif c in 'l':
        newPassword += '1'
    else:
        newPassword += c

print(newPassword)

