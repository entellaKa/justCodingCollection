n, l = map(int, input().split())

answer = []
for i in range(l):
    answer.append(i)

while True:
    if l <= 100 and n >= sum(answer):
        if (n - sum(answer)) % l == 0:
            m = (n - sum(answer)) // l
            for i in answer:
                print(i + m, end=' ')
            break
        else:
            answer.append(l)
            l += 1
    else:
        print('-1 ')
        break
