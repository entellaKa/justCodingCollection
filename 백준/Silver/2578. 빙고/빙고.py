l = []

for i in range(5):
    for j in input().split():
        l.append(j)

answer = 0
cnt = 0
d1 = 0
d2 = 0
for i in range(5):
    for j in input().split():
        if answer+d1+d2 >= 3:
            break
        cnt += 1

        for k in range(25):
            if j == l[k]:
                l[k] = 'x'
                y = 0

                x = k%5
                for m in range(5):
                    if l[m*5+x] == 'x':
                        y += 1
                if y == 5:
                    answer += 1

                x = k//5*5
                y = 0
                for m in range(5):
                    if l[m+x] == 'x':
                        y += 1
                if y == 5:
                    answer += 1

                y = 0
                for m in range(5):
                    if l[m*6] == 'x':
                        y += 1
                if y == 5:
                    d1 = 1

                y = 0
                for m in range(1,6):
                    if l[m*4] == 'x':
                        y += 1
                if y == 5:
                    d2 = 1


print(cnt)