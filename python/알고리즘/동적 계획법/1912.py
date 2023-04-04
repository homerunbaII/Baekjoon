n = int(input())

dp = [0 for i in range(n)]


arr = list(map(int, input().split()))


for i in range(n):
    if i == 0:
        dp[i] = arr[i]
    else:
        if dp[i-1] < 0:
            dp[i] = arr[i]
        else:
            dp[i] = dp[i-1] + arr[i]

print(max(dp))
