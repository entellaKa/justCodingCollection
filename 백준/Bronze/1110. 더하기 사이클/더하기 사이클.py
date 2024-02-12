n = int(input())

x = n//10
y = n%10

answer = 0

m = -1

while m != n:
    z = x + y
    m = y*10+z%10

    x = m // 10
    y = m % 10

    answer += 1
    
print(answer)
