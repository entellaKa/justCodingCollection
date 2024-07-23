input()
l = set(input().split())
input()
for i in input().split():
    if i in l:
        print(1)
    else:
        print(0)