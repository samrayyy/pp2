def even_generator(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield i

def main():
    try:
        n = int(input())
        if n < 0:
            return #negative

        even_numbers = even_generator(n)
        print("Even numbers between 0 and", n, ":", end=" ")
        print(*even_numbers, sep=", ")
    except ValueError:
        print("error")