n = int(input())
l = list(map(int, input().split()))

for i in range(int(input())):
    s, x = map(int, input().split())
    if s == 1:
        for j in range(len(l)):
            if (j+1)%x == 0:
                l[j] = (l[j]+1)%2
    else:
        x-=1
        r = 1
        while x-r>=0 and x+r<len(l):
            if l[x-r] != l[x+r]:
                break
            r+=1

        l[x] = (l[x]+1)%2
        for j in range(1, r):
            l[x-j] = (l[x-j]+1)%2
            l[x+j] = (l[x+j]+1)%2

for i in range(len(l)):
    print(l[i], end=' ')
    if (i+1)%20==0:
        print()
