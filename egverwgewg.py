a = input()
c = 0
for i in range(len(a)):
    if 'abcdefghijklmnopqrstuvwxyz' in a:
        c += 1
print(c)
