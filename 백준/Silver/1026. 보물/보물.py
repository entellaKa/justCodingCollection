n = int(input())
a = sorted(list(map(int,input().split(" "))))
b = sorted(list(map(int,input().split(" "))), reverse=True)

an = 0
for i in range(n):
    an += a[i]*b[i]

print(an)