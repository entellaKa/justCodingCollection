n = int(input())

t = 0
m = 1
l = []
answer = []
for i in range(n):
    k = int(input())
    for j in range(t, k):
        l.append(j+1)
        answer.append("+")
        t+=1
    if k == l.pop():
        answer.append("-")
    else:
        print("NO")
        break
if len(l) == 0 and len(answer) == 2*n:
    for i in answer:
        print(i)