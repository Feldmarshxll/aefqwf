a = int(input())
ch = a % 10
ans = True

while a > 9:
    a //= 10
    ch1 = a % 10
    if ch1 < ch:
        ans = False
        break
    ch = ch1
if ans:
    print("YES")
else:
    print('NO')