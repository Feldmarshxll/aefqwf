c = 0
while True:
    a = int(input())
    if a == 0:
        break
    if a % 6 == 0 and a % 10 == 4:
        c += a
print(c)