n = int(input())
dp = [[0 for i in range(n)] for i in range(n)]
graph = []


for i in range(n):
    graph.append(list(map(int, input().split())))


dp[0][0] = 1

for i in range(n):
    for j in range(n):
        if i == n-1 and j == n-1:
            break
        m = graph[i][j]
        w = dp[i][j]
        if w > 0:
            if i + m < n:
                dp[i + m][j] += w
            if j + m < n:
                dp[i][j + m] += w

print(dp[n-1][n-1])
