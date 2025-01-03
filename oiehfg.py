import math
n = int(input())
for i in range(1, n + 1):
    c = 1
    for j in range(1, 2 * i):
        if math.ceil((2 * i - 1) // 2) >= j:
            print(c, end='')
            c += 1
        else:
            print(c, end='')
            c -= 1
    print()