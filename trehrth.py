a = int(input())
n = 0
while a != 0:
    l = a % 10
    n = n * 10 + l
    a = a // 10
print(n)