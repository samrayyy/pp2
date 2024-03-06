from functools import reduce

def multiply(numbers):
    if not numbers:
        return None
    return reduce(lambda x, y: x * y, numbers)
