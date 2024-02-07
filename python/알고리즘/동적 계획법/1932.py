n = int(input())

dp = [0 for _ in range(n)]

for i in range(n):
    dp[i] = list(map(int, input().split()))



if n == 1:
    print(dp[0][0])
else:
    dp[1][0] += dp[0][0]
    dp[1][1] += dp[0][0]
    for i in range(2, n):
        for j in range(i + 1):
            if j == 0:
                dp[i][j] += dp[i -1][j]
            elif j == i :
                dp[i][j] += dp[i -1][j - 1]
            else:        
                dp[i][j] += max(dp[i -1][j - 1], dp[i - 1][j])
    print(max(dp[n-1]))