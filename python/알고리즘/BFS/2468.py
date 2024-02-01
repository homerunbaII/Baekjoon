from collections import deque
import sys

def bfs(x, y, height):
    visited[x][y] = 1
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]
    q = deque()
    q.append([x,y]) ### 시작지점 찾기
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if visited[nx][ny] == 0 and graph[nx][ny] > height:
                    visited[nx][ny] = 1
                    q.append([nx, ny])

n = int(input())

graph = [list(map(int, input().split())) for _ in range(n)]

## 최대값 찾기
real_max = 0
real_min = 10e9
for i in graph:
    temp_max = max(i)
    temp_min = min(i)
    if temp_max > real_max:
        real_max = temp_max
    if temp_min < real_min:
        real_min = temp_min

max_count = 0
## 최대 높이까지만 수행
for height in range(1, real_max + 1):
    count = 0
    # 시작 지점 찾기
    visited = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            ## 시작지점이 비 수위보다 높아야 시작할 수 있음
            if graph[i][j] > height and visited[i][j] == 0:
                x, y = i, j
                bfs(i,j, height)
                count += 1
    if count > max_count:
        max_count = count
### 모두 잠겼을 때 고려
    
if real_max == real_min:
    print(1)
else:
    print(max_count)
