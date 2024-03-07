import math

def a(n_sides, side_length):
    area = (n_sides * side_length ** 2) / (4 * math.tan(math.pi / n_sides))
    return area

n_sides = int(input())
side_length = float(input())

area = a(n_sides, side_length)
print(area)