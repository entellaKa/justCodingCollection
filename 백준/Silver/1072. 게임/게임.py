import math

x, y = map(int, input().split(" "))
z = y*100//x
if z >=99:
    print(-1)
else:
    n1 = (z+1)*x-100*y
    n2 = (99-z)

    print(math.ceil(n1/n2))
