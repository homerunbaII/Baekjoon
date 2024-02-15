
import sys

input = sys.stdin.readline
sys.setrecursionlimit = (10 ** 8)

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x,y):
    # 끝에 도달하면 경우의 수 1을 리턴
    if x == m - 1 and y == n - 1:
        return 1
    
    # 방문한적이 있으면 그 경우의 수 리턴
    if dp[x][y] != -1:                       
        return dp[x][y]

    ways = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        print(x,y)
        print(nx,ny)
        if 0<= nx < m and 0 <= ny < n:
            if graph[x][y] > graph[nx][ny]:
                ways += dfs(nx,ny)
        
    dp[x][y] = ways
    return ways
                

## 

## 가로 세로
m, n = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(m)]
dp = [[-1 for _ in range(n)] for _ in range(m)]
print(dfs(0,0))
