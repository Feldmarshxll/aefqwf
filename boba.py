n = int(input())
c = 0
matrix = [[int(_) for _ in input().split()] for __ in range(n)]
for i in range(n):
    c += int(matrix[i][i])
print(c)