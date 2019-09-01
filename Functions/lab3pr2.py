
import random

def licensePlate(num_letters):
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    plate = ''
    counter = 0
    while (counter < num_letters):
        plate += random.choice(letters)
        counter += 1
    while (counter < 6):
        plate += str(random.randint(0, 9))
        counter += 1
    return plate


