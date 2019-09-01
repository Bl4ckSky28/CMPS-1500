
#recursive factorial
def factorial_product(n):
    if n <= 1:
        return "1"
    else:
        return str(n) + "*" + factorial_product(n - 1)

def caps(c):
    #assigns ascii value of c to ac
    ac = ord(c)
    if ac > 97 and ac <= 122:
        #returns corresponding letter
        return chr(ac - 32)
    else:
        return c

def allCaps(s):
    if s == '':
        return s
    else:
        return caps(s[0]) + allCaps(s[1:])

