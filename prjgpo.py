row, column = int(input()), int(input())

neo = [[input() for j in range(column)] for i in range(row)]
print('ВЫВОД:')
for r in range(row):
    for c in range(column):
        print(neo[r][c], end=' ')
    print()
print()    
for r in range(column):
    for c in range(row):
        print(neo[c][r], end=' ')
    print()