def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


# function to calculate the average of a list of numbers
def average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)
