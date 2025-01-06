n, r, c = map(int, input().split())


stack = 2
answer = 0
for i in range(n):
    t = 0
    if r%stack >= stack//2:
        t+=2
    if c%stack >= stack//2:
        t+=1

    answer += 4**i*t
    stack *= 2
print(answer)
