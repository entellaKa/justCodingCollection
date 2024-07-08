a = int(input())
b = int(input())
c = int(input())

print(a+b-c)
if b < 10:
    print(a*10+b-c)
elif b < 100:
    print(a*100+b-c)
elif b < 1000:
    print(a*1000+b-c)
else:
    print(a*10000+b-c)