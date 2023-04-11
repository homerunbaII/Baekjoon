n, m = map(int, input().split())

dp = [0] * (n ** 2+1)

cnt = 0

for i in range(1, n + 1):
    arr = list(map(int, input().split()))  # 0 1 2 3
    for j in range(1, n + 1):  # 1 2 3 4
        dp[cnt * n + j] = dp[cnt * n + j - 1] + arr[j - 1]
    cnt += 1

print(dp)

for i in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    result = dp[x2][y2] - dp[x1-1][y2] - dp[x2][y1-1] + dp[x1-1][y1-1]
    print(result)
