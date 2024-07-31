t = int(input())

for i in range(t):
    input()
    arr = list(map(int, input().split()))
    
    print(min(arr), max(arr))