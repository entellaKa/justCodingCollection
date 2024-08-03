n = int(input())

l = []

bombClick = 0

for i in range(n):
    l.append(input())

for i in range(n):
    s = input()

    for j in range(n):
        bomb = 0

        if s[j] == 'x':
            if l[i][j] == "*":
                bombClick = 1
                continue
                
            if i != 0:
                if j != 0:
                    if l[i-1][j-1] == '*':
                        bomb += 1
                if l[i-1][j] == '*':
                    bomb += 1
                if j+1 != n:
                    if l[i-1][j+1] == '*':
                        bomb += 1

            if j != 0:
                if l[i][j-1] == '*':
                    bomb += 1
            if j+1 != n:
                if l[i][j+1] == '*':
                    bomb += 1

            if i+1 != n:
                if j != 0:
                    if l[i+1][j-1] == '*':
                        bomb += 1
                if l[i+1][j] == '*':
                    bomb += 1
                if j+1 != n:
                    if l[i+1][j+1] == '*':
                        bomb += 1

            l[i] = l[i][:j]+str(bomb)+l[i][j+1:]

if bombClick == 0:
    for i in range(len(l)):
        l[i] = l[i].replace('*', ".")

for i in l:
    print(i)
