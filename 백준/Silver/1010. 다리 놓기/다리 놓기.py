k = int(input())

for z in range(k):
    n, m = map(int, input().split(" "))

    x = 1
    for i in range(m,n,-1):
        x*=i
    for i in range(1, m-n+1):
        x//=i
    print(x)