def squares(a, b):
    for i in range(a, b + 1):
        yield i ** 2

a = int(input("vvesti chislo"))
b = int(input("vvesti chislo"))
print(f"Squares of numbers from {a} to {b}:")
for square in squares(a, b):
    print(square)