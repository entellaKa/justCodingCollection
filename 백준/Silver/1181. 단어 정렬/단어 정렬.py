l = set()

for i in range(int(input())):
    l.add(input())
sort1 = sorted(l)
for i in sorted(sort1, key=len):
    print(i)
