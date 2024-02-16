import sys

input = sys.stdin.readline

n = int(input())

dp = [0 for _ in range(n + 1)]
max_dp = 0
for i in range(n):
    day, cost = map(int,input().split())
    if dp[i] > max_dp:
        max_dp = dp[i]
    if dp[i] < max_dp:
        dp[i] = max_dp
    if (i + day) <= n:
        if dp[i +day] < dp[i] + cost :
            dp[i + day] = dp[i] + cost

print(max(dp))