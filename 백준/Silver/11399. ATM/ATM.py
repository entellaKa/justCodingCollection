input()
l = list(map(int, input().split()))
l.sort()

an = 0
stack = 0
for i in l:
    stack+=i
    an+=stack
print(an)