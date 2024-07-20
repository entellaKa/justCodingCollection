n = int(input())
isis = 0

for i in range(1000):
    a = b = n - (1000 - i)
    if a < 1: 
        continue
    while a != 0:
        b += a%10
        a //= 10
    if b == n:
        print(n - (1000 - i))
        isis = 1
        break

if isis == 0:
    print(0)
