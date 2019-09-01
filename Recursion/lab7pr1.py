
def uppercount(s):
    uppers = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if s == "":
        return 0
    #recursive case if first character is uppercase
    elif s[0] in uppers:
        return 1 + uppercount(s[1:])
    #recursive case if first character is not uppercase
    else:
        return 0 + uppercount(s[1:])

def clean_string(s):
    clean = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz '
    if s == "":
        return s
    #recursive case if first character is acceptable
    elif s[0] in clean:
        return s[0] + clean_string(s[1:])
    #recursive case if first character is not acceptable
    else:
        return clean_string(s[1:])

def clean_list(l1, l2):
    #base case
    if l1 == l2:
        return []
    #alternative case
    elif not l1:
        return []
    #recursive case if first item is in l2
    elif l1[0] not in l2: 
        return [l1[0]] + clean_list(l1[1:], l2)
    #recursive case if first item is not in l2
    else:
        return clean_list(l1[1:], l2)


    
