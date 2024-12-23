n = int(input())

s = 0
c = 0
p = 1
l = n % 10 
f = n

while n > 0:
    d = n % 10
    s += d
    c += 1
    p *= d
    fd = d  
    n = n // 10
a = s / c
fls = fd + l
print(s)  
print(c)  
print(p)  
print(a)  
print(fd) 
print(fls)  
