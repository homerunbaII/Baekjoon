from collections import deque

m, n, rectangle = map(int, input().split())
visited = [[0] * n for _ in range(m)]
graph = [[1] * n for _ in range(m)]
draw = []

def bfs(x, y):
    count = 1
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]
    q = deque()
    q.append([x,y])
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx < m and 0<= ny < n:
                if visited[nx][ny] == 0 and graph[nx][ny] == 1:
                    visited[nx][ny] = 1
                    count += 1
                    q.append([nx,ny])
    return count



## 좌표 x,y 다른거 유의
# 입력받은 위치 시작 이상 입력받은 위치 마지맞 미만
for _ in range(rectangle):
    start_y, start_x, end_y, end_x = map(int, input().split())
    for i in range(start_x, end_x):
        for j in range(start_y, end_y):
            graph[i][j] = 0

for i in range(m):
    for j in range(n):
        if visited[i][j] == 0 and graph[i][j] == 1:
            visited[i][j] = 1
            c = bfs(i,j)
            draw.append(c)

draw.sort()

print(len(draw))
print(*draw)
    
