

def get_header(width, height):
    return 'P3\n' + str(width) + ' ' + str(height) + '\n' + '255\n'

def netherlands(width, height):
    flag = ''
    red = '255 0 0 '
    white = '255 255 255 '
    blue = '0 0 255 '

    height /= 3
    height = int(height)

    value = height * width
        
    flag += red * value
    flag += white * value
    flag += blue * value

    return flag

def nigeria(width, height):
    flag = ''
    green = '0 255 0 '
    white = '255 255 255 '
    black = '0 0 0 '
    red = '255 0 0 '

    width /= 3
    width = int(width)
    
    while height > 0:
        flag += green * width
        flag += white * width
        flag += green * width
        height -= 1

    return flag

def uae(width, height):
    flag = ''
    red = '255 0 0 '
    green = '0 255 0 '
    white = '255 255 255 '
    black = '0 0 0 '

    for x in range(height // 3):
        for x in range(width // 4):
            flag += red
        for x in range(3 * (width // 4)):
            flag += green
    for x in range(height // 3):
        for x in range(width // 4):
            flag += red
        for x in range(3 * (width // 4)):
            flag += white
    for x in range(height // 3):
        for x in range(width // 4):
            flag += red
        for x in range(3 * (width // 4)):
            flag += black

    return flag

    
def main():
    width = int(input("Please, enter width: "))
    height = int(input("Please, enter height: "))
    file = input("Please, enter output file name: ")

    myFile = open(file, 'w')
    myFile.write(get_header(width, height))
    myFile.write(uae(width, height))
    myFile.close()

    print("The output has been written to", file)
    print("View the result in XnView.")

main()


