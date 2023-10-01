l = 64
r = l
n = int(input())
answer = 1

while r != n:
    l = l//2
    if r > n:
        r -= l
    else:
        r += l
        answer+=1
        
print(answer)