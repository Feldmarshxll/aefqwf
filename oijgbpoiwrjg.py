import math
def newton_per_square_meter(row):
    numbers = []
    counter_row = row + 1
    for i in range(counter_row):
        numbers.append(int(math.factorial(row) / (math.factorial(i) * math.factorial(row - i))))
    return numbers
print(newton_per_square_meter(int(input())))


