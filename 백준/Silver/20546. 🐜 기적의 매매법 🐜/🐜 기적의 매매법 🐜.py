m = n = int(input())

l = list(map(int, input().split()))

bnp = 0
timing = 0
asc = 0
stack = l[0]

for i in l:
    if m >= i:
        bnp += m//i
        m = m%i

    if stack == i:
        asc = 0
    elif stack < i:
        if asc == 1:
            asc = 2
        elif asc == 2:
            n += i*timing
            timing = 0
        else:
            asc = 1
    elif stack > i:
        if asc == -1:
            asc = -2
        elif asc == -2:
            timing += n//i
            n = n%i
        else:
            asc = -1
    stack = i

m += bnp*l[-1]
n += timing*l[-1]

if m == n:
    print("SAMESAME")
elif m > n:
    print("BNP")
else:
    print("TIMING")