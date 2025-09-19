n = int(input())
c = 0 
matrix = [[int(_) for _ in input().split()] for __ in range(n)]

for i in range(n):
    lob = 0
    c = sum(matrix[i]) // n
    for j in range(n):
        if matrix[i][j] > c:
            lob += 1
    print(lob)
