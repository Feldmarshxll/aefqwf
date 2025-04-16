def multiplication_float(a, b):
    c = 0
    s = 0
    while a != int(a):
        a *= 10
        c += 1
    while b != int(b):
        b *= 10
        s += 1
    return (int(a) * int(b)) / (10 ** (c + s))

a = float(input())
b = float(input())
result = multiplication_float(a, b)
print(result)

