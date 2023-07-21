n, m = map(int, input().split(" "))
board = []

for i in range(n):
    board.append(input())

arr = [[0] * (m - 7) for i in range(n - 7)]

a = "BW" * 4
b = "WB" * 4

bw1 = 0
wb1 = 0

for i in range(n - 7):
    for j in range(m - 7):
        for k in range(8):
            c = a
            a = b
            b = c
            for l in range(8):
                if board[i + k][j + l] != c[l]:
                    arr[i][j] += 1

# print(min(min(arr)))
# print(max(max(arr)))
# print(arr)
answer = 32
for i in arr:
    t = min(i)
    if answer > t:
        answer = t
    t = 64 - max(i)
    if answer > t:
        answer = t
print(answer)
