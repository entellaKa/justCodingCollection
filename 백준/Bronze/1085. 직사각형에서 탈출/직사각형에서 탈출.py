x,y,w,h = map(int, input().split(" "))

w-=x
h-=y
a = sorted([x,y,w,h])
print(a[0])