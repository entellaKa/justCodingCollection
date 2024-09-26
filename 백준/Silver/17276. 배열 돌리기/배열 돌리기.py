t = int(input())

for _ in range(t):
    n, theta = map(int, input().split())

    l = []
    for i in range(n):
        l.append(list(map(int, input().split())))

    theta = (theta + 360) % 360 // 45

    for i in range(theta):
        for i in range(n//2):
            j=i+1
            x = y = n//2

            t = l[y][x+j]
            l[y][x+j] = l[y-j][x+j]
            l[y-j][x+j] = l[y-j][x]
            l[y-j][x] = l[y-j][x-j]
            l[y-j][x-j] = l[y][x-j]
            l[y][x-j] = l[y+j][x-j]
            l[y+j][x-j] = l[y+j][x]
            l[y+j][x] = l[y+j][x+j]
            l[y+j][x+j] = t

    for i in l:
        for j in i:
            print(j, end=' ')
        print()