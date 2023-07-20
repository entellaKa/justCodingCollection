n = int(input())
strings = []

for i in range(n):
    strings.append(input())

answer = ""
for i in range(len(strings[0])):
    b = True
    k = strings[0][i]
    for j in range(n-1):
        if strings[j+1][i] != k:
            b = False
    if b:
        answer+=strings[0][i]
    else:
        answer+="?"
print(answer)