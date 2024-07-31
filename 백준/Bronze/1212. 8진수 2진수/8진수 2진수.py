n = input()
if n == '0':
    print(0)
i = n[0]
n = n[1:]
if i == '1':
    print('1', end='')
elif i == '2':
    print('10', end='')
elif i == '3':
    print('11', end='')
elif i == '4':
    print('100', end='')
elif i == '5':
    print('101', end='')
elif i == '6':
    print('110', end='')
elif i == '7':
    print('111', end='')

for i in n:
    if i == '0':
        print('000', end='')
    elif i == '1':
        print('001', end='')
    elif i == '2':
        print('010', end='')
    elif i == '3':
        print('011', end='')
    elif i == '4':
        print('100', end='')
    elif i == '5':
        print('101', end='')
    elif i == '6':
        print('110', end='')
    elif i == '7':
        print('111', end='')