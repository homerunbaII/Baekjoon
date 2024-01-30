from collections import deque

def bfs (x,y):
    dx = [1, -1, 0, 0]
    dy = [0 ,0 ,-1, 1]
    q = deque()
    q.append([x,y])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx < n and 0 <= ny < m:
                if visited[nx][ny] == 0 and graph[nx][ny] == 1:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append([nx,ny])
    return visited





n,m = map(int, input().split())
graph = [list(map(int, list(input()))) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
visited[0][0] = 1

a = bfs(0,0)
print(a)