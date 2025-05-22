m = []
n = int(input())
for _ in range(n):
    a = int(input())
    if a % 10 == 9:
        m.append(a)
print(max(m))