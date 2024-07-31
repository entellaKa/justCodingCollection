n = int(input())

answer = 0

x = [-1]*11

for i in range(n):
    a,b = map(int, input().split())
    
    if b == 1 and x[a] == 0:
        answer += 1
    elif b == 0 and x[a] == 1:
        answer += 1
    
    x[a] = b
print(answer)