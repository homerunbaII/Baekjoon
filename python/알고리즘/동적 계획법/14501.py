n = int(input())

consult_list = [0]
dp = [0 for _ in range(n + 2)]
for i in range(1, n + 1):
    day, cost  = map(int,input().split())
    dp[i] = max(dp[:i + 1])
    if i + day <= n + 1:
        if dp[i + day] < dp[i] + cost :
            dp[i + day] = dp[i] + cost

print(dp)
