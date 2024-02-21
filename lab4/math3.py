import math

def a(n_sides, side_length):
    area = (n_sides * side_length ** 2) / (4 * math.tan(math.pi / n_sides))
    return area

n_sides = int(input("Input number of sides: "))
side_length = float(input("Input the length of a side: "))

area = a(n_sides, side_length)
print("The area of the polygon is:", area)
