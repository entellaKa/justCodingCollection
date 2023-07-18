t = int(input())

for i in range(t):
    cnt = 0
    x1, y1, x2, y2 = map(int, input().split(" "))
    n = int(input())
    for j in range(n):
        cx, cy, r = map(int, input().split(" "))
        rr = r**2
        r1 = (cx-x1)**2+(cy-y1)**2 < rr
        r2 = (cx-x2)**2+(cy-y2)**2 < rr
        if (not(r1) and r2) or (r1 and not(r2)):
            cnt+=1
    print(cnt)