n,m = map(int, input().split())
arr = []
for i in range(n):
    arr.append(input())

answer = 1

for i in range(n-1):
    for j in range(m-1):
        t = arr[i][j+1:]
        for k in range(len(t)):
            if t[k] == arr[i][j]:
                if n <= k + i + 1:
                    break
                k+=1
                if arr[i+k][j] == arr[i][j]:
                    if arr[i+k][j+k] == arr[i][j]:
                        if answer <= k:
                            answer = k+1
print(answer**2)
                