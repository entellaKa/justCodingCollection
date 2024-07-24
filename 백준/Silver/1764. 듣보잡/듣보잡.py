n, m = map(int, input().split())

듣 = set([])
듣보 = []

for i in range(n):
    듣.add(input())

for i in range(m):
    k = input()
    if k in 듣:
        듣보.append(k)

print(len(듣보))
듣보.sort()
for i in 듣보:
    print(i)