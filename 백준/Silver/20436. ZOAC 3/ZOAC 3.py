a,b = map(str, input().split())
s = input()

keys = ['qwertyuiop','asdfghjkl','zxcvbnm']

for i in range(3):
    for j in range(len(keys[i])):
        if keys[i][j] == a:
            x1 = j
            y1 = i
        if keys[i][j] == b:
            x2 = j
            y2 = i

answer = len(s)
for k in s:
    for i in range(3):
        for j in range(len(keys[i])):
            if keys[i][j] == k:
                x = j
                y = i
                
                if k in 'qwertasdfgzxcv':
                    answer+=abs(x-x1)+abs(y-y1)
                    x1 = x
                    y1 = y
                else:
                    answer+=abs(x-x2)+abs(y-y2)
                    x2 = x
                    y2 = y
print(answer)