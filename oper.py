symbols = input().split()
sublists = [[]]
for i in range(len(symbols)):
    for j in range(i + 1, len(symbols) + 1):
        sublists.append(symbols[i:j])
print(sublists)