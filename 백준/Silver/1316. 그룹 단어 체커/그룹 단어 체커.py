n = int(input())

answer = 0
for i in range(n):
    answer+=1
    word = input()
    group = []
    t = ''
    for c in word:
        if c != t:
            if c in group:
                answer-=1
                break
            else:
                group.append(c)
                t = c

print(answer)