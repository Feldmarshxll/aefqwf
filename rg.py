n = int(input())
for i in range(1, n + 1):
    c = 0
    for j in range(1):
        if n % i == 0:
            c += 1
    print(i, '+' * c)