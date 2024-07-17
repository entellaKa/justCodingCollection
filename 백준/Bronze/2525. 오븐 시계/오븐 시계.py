h, m = map(int, input().split())
time = int(input())

m += time % 60
if m >= 60:
    m-=60
    h+=1
h = (h+time//60)%24

print(h, m)
