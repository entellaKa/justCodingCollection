n = int(input())
x = 1
while n > x:
    x<<=1
    
if x == n:
    print(n)
else:
    print((n-(x>>1))*2)