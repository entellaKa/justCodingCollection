a, b = map(int, input().split())

if b > a:
    t = a
    a = b
    b = t

m=a*b
while True:
    if a%b == 0:
        break;
    r = a%b
    a = b
    b = r
print(b)
print(m//b)