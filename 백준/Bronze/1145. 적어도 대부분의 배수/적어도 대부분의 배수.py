ar = list(map(int, input().split(' ')))

c = 0
i = 1
while c<3:
    c = 0
    i+=1

    for n in ar:
        if i%n==0:
            c+=1
print(i)
