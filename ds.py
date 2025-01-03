a, b = int(input()), int(input())
max_sum = 0
num = 0
for i in range(b, a, -1):
    sum = 0
    for j in range(1, i + 1):
        if i % j == 0:
            sum += j
    if max_sum < sum:
        num = i
        max_sum = sum
print(num, max_sum)