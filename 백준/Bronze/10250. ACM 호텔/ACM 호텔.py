t = int(input())
for i in range(t):
    h, w, n = map(int,input().split())
    x = n//h+1
    y = n%h
    if y == 0:
        y = h
        x-=1
    print(y*100+x)