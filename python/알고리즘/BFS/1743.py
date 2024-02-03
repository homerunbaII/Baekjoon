from collections import deque


def bfs(x,y):
    q = deque()
    q.append([x,y])
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]
    visited[x][y] = 1
    count = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx < n and 0<= ny < m:
                if visited[nx][ny] == 0 and graph[nx][ny] == 1:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append([nx,ny])
                    count += 1
    return count


n , m, trash = map(int,input().split())
visited = [[0 for _ in range(m)] for _ in range(n)]
graph = [[0 for _ in range(m)] for _ in range(n)]

for  _ in range(trash):
    x , y = map(int, input().split())
    x = x - 1
    y = y - 1
    graph[x][y] = 1

area = []
for i in range(n):
    for j in range(m):
        if visited[i][j] == 0 and graph[i][j] == 1:
            a = bfs(i,j)
            area.append(a)
print()
print(max(area))
