n, m = map(int, input().split(" "))
arr = list(map(int, input().split(" ")))
#arr = [1,2,3,4]

for i in range(n-1, 0, -1):
    for j in range(i):
        if arr[j] > arr[j+1]:
            t = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = t
            
def out(n, m, arr, t):
    if m==0:
        print(t.lstrip())
        return
    for i in range(n):
        out(n-1, m-1, arr[:i]+arr[i+1:], t+" "+str(arr[i]))

out(n,m,arr,"")  