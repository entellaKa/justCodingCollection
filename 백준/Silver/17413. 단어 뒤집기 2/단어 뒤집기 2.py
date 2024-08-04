s = input()

ans = ''
t = ''
r = 0
for i in s:
    if i == '<':
        ans += t[::-1] + '<'
        t = ''
        r = 1
    elif i == '>':
        ans += t+'>'
        t = ''
        r = 0
    elif i == ' ':
        if r == 0:
            ans += t[::-1]+' '
            t = ''
        else:
            ans += t+' '
            t = ''
    else:
        t += i
if r == 0:
    ans += t[::-1]
else:
    ans += t+'>'

print(ans)
