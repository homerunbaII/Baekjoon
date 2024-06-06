n = int(input())

dp = [0] * 1000002
dp[1] = 1
dp[2] = 2
for i in range(2 ,n + 2):
    dp[i] = dp[i-1] + dp[i-2]
    dp[i] %= 15746

print(dp[n + 1])