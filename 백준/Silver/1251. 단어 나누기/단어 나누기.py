word = list(input())

arr = []
for i in range(1, len(word)-1):
    w1 = word[:i]
    w1.reverse()
    for j in range(i+1, len(word)):
        w2 = word[i:j]
        w3 = word[j:]
        w2.reverse()
        w3.reverse()

        temp = w1 + w2 + w3
        arr.append(''.join(temp))
print(sorted(arr)[0])