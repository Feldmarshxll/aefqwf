a = int(input())
while a % 7 == 0:
    print(a)
    a = int(input())
    if a % 7 != 0:
        break
