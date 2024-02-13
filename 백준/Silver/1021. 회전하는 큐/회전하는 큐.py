n, m = map(int, input().split())
q = [x for x in range(1, n+1)]

answer = 0
nums = list(map(int, input().split()))

for v in nums:
    i = q.index(v)
    answer += min(i, len(q)-i)
    q = q[i:] + q[:i]
    q.pop(0)
print(answer)

