m = []
n = int(input())
for i in range(n):
    a = int(input())
    if a % 10 == 3:
        m.append(a)
print(max(m))