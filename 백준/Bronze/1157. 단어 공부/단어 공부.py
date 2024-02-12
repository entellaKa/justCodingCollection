text = list(input().upper())
alphabet = list('poiuytrewqlkjhgfdsamnbvcxz'.upper())

alpha = {}
for i in alphabet:
    alpha[i] = 0

for c in text:
    alpha[c] +=1

maxAlpha = sorted(alpha, key=lambda x: alpha[x], reverse=True)
if alpha[maxAlpha[0]] == alpha[maxAlpha[1]]:
    print("?")
else:
    print(maxAlpha[0])

