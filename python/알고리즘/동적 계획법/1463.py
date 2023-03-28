n = int(input())

dp = [0] * (n + 1)

dp[1] = 0


for i in range(2, n + 1):
    val1 = 1e9
    val2 = 1e9
    val3 = 1e9
    if i % 3 == 0:
        val1 = dp[i // 3]
    if i % 2 == 0:
        val2 = dp[i // 2]
    val3 = dp[i - 1]
    dp[i] = min(val1, val2, val3) + 1


print(dp[n])
