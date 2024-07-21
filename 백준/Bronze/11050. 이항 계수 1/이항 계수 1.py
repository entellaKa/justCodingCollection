a, b = map(int, input().split())
an = 1
for i in range(b):
    an*=a-i
    an//=i+1
print(an)