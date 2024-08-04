n, m = map(int, input().split())
s = list(map(int, input().split()))
d = list(map(int, input().split()))

for i in range(m):
    p = [0]*n
    for j in range(n):
        #s[j] = p[d[j]]
        p[d[j]-1] = s[j]
    s = p

for i in s:
    print(i, end=' ')