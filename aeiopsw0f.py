n = int(input())
c = 0
for i in range(n):
    a = int(input())
    if a % 6 == 0:
        c += a
print(c)