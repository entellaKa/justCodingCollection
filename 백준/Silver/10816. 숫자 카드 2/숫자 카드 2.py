input()
ns = list(map(int, input().split()))
input()
ms = list(map(int, input().split()))

d = {}
for i in ms:
    d[i] = 0

for i in ns:
    if i in d:
        d[i] += 1

for i in ms:
    print(d[i], end=' ')