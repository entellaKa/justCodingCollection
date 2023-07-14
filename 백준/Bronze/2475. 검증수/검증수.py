a = list(map(int, input().split(" ")))
n = 0
for i in a:
    n+=i**2
print(n%10)