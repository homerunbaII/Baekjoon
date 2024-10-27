n = int(input())

dp = [[0 for _ in range(10)] for _ in range(n + 1)]
dp[0] = [1,1,1,1,1,1,1,1,1,1] 

answer = 0

for i in range(1,n + 1):
    for j in range(1, 10):
        for k in range(1, j + 1):
            dp[i][j] += dp[i-1][k]



for i in range(n):
    answer += (sum(dp[i]) % 10007)

print(answer)
