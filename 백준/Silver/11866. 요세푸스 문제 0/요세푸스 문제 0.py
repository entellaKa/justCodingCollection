n, k = map(int, input().split())
l = [x+1 for x in range(n)]
print(end='<')
for i in range(n-1):
    for j in range(k-1):
        l.append(l.pop(0))
    print(l.pop(0), end=', ')
print(l.pop(), end='>')