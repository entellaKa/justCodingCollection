n, a = map(int, input().split(" "))
r = n - 1
    
def pow1(x, y):
    n = 1
    while y > 0:
        if y&1==1:
            n*=x
        x*=x
        y>>=1
        x%=1000000007
    return n


l = pow1(n, a)
b = pow1(r, a)

an = l+(n-2)*(l-b)

print(an*n%1000000007)

