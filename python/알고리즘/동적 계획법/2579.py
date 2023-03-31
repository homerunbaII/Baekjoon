n = int(input())

dp = [0] * (n + 4)
s = [0] * (n + 4)

for i in range(1, n + 1):
    s[i] = int(input())

dp[1] = s[1]
dp[2] = s[1] + s[2]
dp[3] = max(s[1] + s[3], s[2] + s[3])

if n > 3:
    for i in range(4, n+1):
        dp[i] = max(dp[i-3] + s[i-1] + s[i], dp[i-2] + s[i])

print(dp[n])
