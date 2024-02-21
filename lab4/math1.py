import math

def dradian(degree):
    radian = degree * (math.pi / 180)
    return radian

degree = int(input())
radian = dradian(degree)
print("Input degree:", degree)
print("Output radian:", radian)

