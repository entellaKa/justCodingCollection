quack = {'u': 'a', 'a': 'c', 'c':'k'}

t = input()

ducks = []

answer = -1
n = 0
for i in t:
    if i == 'q':
        ducks.append('u')
        answer = max(answer, len(ducks))
    else:
        if len(ducks) == 0:
            print(-1)
            exit()
        b = 1
        for d in range(len(ducks)):
            if ducks[d] == i:
                if i == 'k':
                    ducks.pop(d)
                else:
                    ducks[d] = quack[i]
                break

if len(ducks) != 0:
    print(-1)
else:
    print(answer)

