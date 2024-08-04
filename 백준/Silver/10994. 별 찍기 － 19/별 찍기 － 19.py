n = int(input())

l = []

for i in range(4*n-3):
    l.append(['*']*(4*n-3))

for i in range(1, 2*n-1):
    if i%2==1:
        for j in range(i, 4*n-3-i):
            l[i][j] = ' '
            l[j][i] = ' '
            l[4*n-3-i-1][j] = ' '
            l[j][4*n-3-i-1] = ' '

for i in l:
    for j in i:
        print(j, end='')
    print()