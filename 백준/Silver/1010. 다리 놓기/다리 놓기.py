k = int(input())

for z in range(k):
    n, m = map(int, input().split(" "))

    k = 1
    for i in range(m,n,-1):
        k*=i
    for i in range(1, m-n+1):
        k//=i
    print(k)