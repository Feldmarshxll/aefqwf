a = int(input())
c = 0
for i in range(2, a + 1):
    if i % a == 0:
        c = i
        break
print(c) 