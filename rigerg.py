row, column = int(input()), int(input())

neo = [[input() for j in range(column)] for i in range(row)]

for r in range(row):
    for c in range(column):
        print(neo[r][c], end=' ')
    print()
