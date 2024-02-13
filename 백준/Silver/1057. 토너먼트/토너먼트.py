n, x, y = map(int, input().split())

answer = 1

if x > y:
    t = x
    x = y
    y = t

while True:

    if x // 2 + 1 == y // 2 and x + 1 == y:
        break
    else:
        x = (x + 1) // 2
        y = (y + 1) // 2
        answer += 1
print(answer)
