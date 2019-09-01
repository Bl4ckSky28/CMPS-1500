
import math

def area(radius):
    area = (radius ** 2) * math.pi
    return area

def cost_per_square_inch(diameter, price):
    radius = diameter / 2
    square_inches = area(radius)
    cost = price / square_inches
    return round(cost, 2)

diameter = float(input("Please enter the diameter of your pizza, in inches: "))
price = float(input("Please enter its cost, in dollars: "))
print("The cost is", cost_per_square_inch(diameter, price), "dollars per square inch.")
