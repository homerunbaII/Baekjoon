n, m = map(int, input().split())

dp = [0] * (n + 1)

dp[0] = 1
dp[1] = 1

for i in range(2, n + 1):
    dp[i] = i * dp[i - 1]

comb = dp[n] // (dp[n-m] * dp[m])

print(comb)
