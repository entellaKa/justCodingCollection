s = input()

for i in range(26):
    if chr(97+i) in s:
        print(s.index(chr(97+i)), end=' ')
    else:
        print(-1, end=' ')