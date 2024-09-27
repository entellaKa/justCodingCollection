class work:
    def __init__(self,s,e):
        self.s = s
        self.e = e

t = int(input())

answer = 0

l = []

cal = []

for x in range(t):
    cal.append([False]*365)
    n, m = map(int, input().split())
    for i in range(len(l)):
        if l[i].s > n:
            l.insert(i, work(n,m))
            break
        elif l[i].s == n:
            if l[i].e <= m:
                l.insert(i, work(n,m))
                break
    if x >= len(l):
        l.append(work(n,m))


h = 1
s = l[0].s-1
ma = 0
for i in l:
    for y in range(t):
        if not cal[y][i.s-1]:
            if y == 0:
                for x1 in range(s, i.s-1):
                    check = True
                    for y1 in range(t):
                        if cal[y1][x1]:
                            check = False
                            break
                    if check:
                        answer += h * (x1-s)
                        h = 1
                        s = i.s-1
                        break
            h = max(h, y+1)
            for x in range(i.s-1, i.e):
                cal[y][x] = True
            break
    ma = max(ma, i.e)

answer += (ma - s) * h
print(answer)