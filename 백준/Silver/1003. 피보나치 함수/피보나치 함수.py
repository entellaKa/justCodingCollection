n = int(input())


def f(n):
    z = x = c = 1
    if n==0:
        print(1,0)
    elif n==1:
        print(0,1)
    else:
        for i in range(n-1):
            z=x+c
            c=x
            x=z
            
        print(x-c,c)

for i in range(n):
    f(int(input()))
