def ta(height, base1, base2):
    area = 0.5 * (base1 + base2) * height
    return area

height = int(input())
base1 = int(input())
base2 = int(input())

area = ta(height, base1, base2)
print("Height:", height)
print("Base, first value:", base1)
print("Base, second value:", base2)
print("Expected Output:", area)
