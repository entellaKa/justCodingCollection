t = int(input())

for i in range(t):
    q = input()
    score = 0
    s = 1
    for j in q:
        if j == 'O':
            score+=s
            s+=1
        else:
            s=1
    print(score)