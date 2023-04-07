import sys

input = sys.stdin.readline

n, k = map(int, input().split())
s = list(map(int, input().split()))

dp = [0 for _ in range(n)]
check = k
cnt = 0

for i in range(n):
    if s[i] % 2 == 0:
        dp[i] = 1
    else:
        dp[i] = -1

for i in range(n):
    j = 0
    while (check >= 0 and i + j < n):
        if dp[i + j] == 1:
            cnt += 1
        if dp[i + j] == -1:
            check -= 1
        j += 1
    dp[i] = cnt
    cnt = 0
    check = k


print(max(dp))
