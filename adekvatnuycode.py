words = input().split()
set1 = set(words[0])
set2 = set(words[1])
set3 = set(words[2])
if set1 == set2 == set3:
    print("YES")
else:
    print("NO")