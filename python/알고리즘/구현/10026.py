from collections import deque

n = int(input())

grid = []
visited = [[0 for _ in range(n)] for _ in range(n)]
visited_x = [[0 for _ in range(n)] for _ in range(n)]
o_cnt = 0
x_cnt = 0


dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

for i in range(n):
    grid.append(list(input()))
    
# 정상
def bfs(a, b, color):
    q = deque()
    q.append([a,b])
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx < n and 0 <= ny < n:
                if visited[nx][ny] == 0:
                    if grid[nx][ny] == color:
                        visited[nx][ny] = 1
                        q.append([nx,ny])
                        
# 색약
def bfs_x(a, b, color_1, color_2):
    q = deque()
    q.append([a,b])
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx < n and 0 <= ny < n:
                if visited_x[nx][ny] == 0:
                    if grid[nx][ny] == color_1 or grid[nx][ny] == color_2:
                        visited_x[nx][ny] = 1
                        q.append([nx,ny])

# 정상
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            visited[i][j] = 1
            bfs(i,j,grid[i][j])
            o_cnt += 1

# 색약
for i in range(n):
    for j in range(n):
        if visited_x[i][j] == 0:
            visited_x[i][j] = 1
            if grid[i][j] == 'R' or grid[i][j] == 'G':
                bfs_x(i,j,'R','G')
                x_cnt += 1
            else:
                bfs_x(i,j,'B,','B')
                x_cnt += 1



print(o_cnt, x_cnt)        
        
