n = int(input())
array = list(map(int, input().split(" ")))

def isPrime(n):
    if n < 2:
        return 0
    i = 2
    while i*i<=n:
        if n % i == 0:
            return 0
        i+=1
    return 1

answer = 0
for n in array:
    answer += isPrime(n)

print(answer)