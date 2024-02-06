from collections import deque
n = int(input())
home = [list(map(int, input().split())) for _ in range(n)]
# 마지막이 가로, 세로, 대각선
dp = [[[0,0,0] for _ in range(n)] for _ in range(n)]
dp[0][1][0] = 1
# 가로 행의 초기화
for i in range(2, n):
    if home[0][i] == 0:
        dp[0][i][0] = dp[0][i-1][0]

for x in range(1, n):
    for y in range(1, n):
        if home[x][y] == 0 and home[x-1][y] == 0 and home[x][y-1] == 0:
            dp[x][y][2] =  dp[x-1][y-1][0] + dp[x-1][y-1][1] + dp[x-1][y-1][2]
        if home[x][y] == 0:
            dp[x][y][0] = dp[x][y-1][0] + dp[x][y-1][2]
            dp[x][y][1] = dp[x-1][y][1] + dp[x-1][y][2]
print(dp)
result = sum(dp[n-1][n-1][i] for i in range(3))
print(result)
