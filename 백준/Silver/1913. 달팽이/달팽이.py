n = int(input())
t = int(input())
nn = n**2

answer = []

for i in range(n//2+1):
    l = [nn-i]
    m = n - 2 * (i+1)
    mm = m**2
    for j in range(i):
        l.append(answer[i-1][j+1]-1)
    for j in range(1, n-i*2):
        l.append(mm+j)
    for j in range(n-i, n):
        l.append(answer[i-1][j]+1)
    answer.append(l)
    for j in range(n):
        print(l[j], end=' ')
        if l[j] == t:
            y = i + 1
            x = j + 1
    print()

for i in range(n//2):
    l = []
    for j in range(n//2-i):
        l.append(answer[n//2+i][j]-1)
    for j in range((i+1)*2):
        l.append(l[-1]-1)
    for j in range(n//2+i+2, n):
        l.append(answer[n//2+i][j]+1)
    answer.append(l)
    for j in range(n):
        print(l[j], end=' ')
        if l[j] == t:
            y = n//2 + i + 2
            x = j + 1
    print()
print(y, x)
