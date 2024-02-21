def divisible(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

def main():
    try:
        n = int(input("vvesti chislo"))
        if n < 0:
            print("negative")
            return

        divisible_numbers = divisible(n)
        print("Numbers divisible by3 and 4 between 0 and", n, ":")
        for number in divisible_numbers:
            print(number)