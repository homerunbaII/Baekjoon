from collections import deque

y, x = map(int,input().split())

graph = []
visited = [[0 for _ in range(y)] for _ in range(x)]
tmt_start = []
tmt_total = x * y
tmt_cnt = 0

for i in range(x):
    tmt_list = list(map(int, input().split()))
    for j in range(y):
        if tmt_list[j] == 1:
            tmt_start.append([i,j])
            visited[i][j] = 1
            tmt_cnt +=1
        if tmt_list[j] == -1:
            tmt_total -= 1
    graph.append(tmt_list)
    

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
q = deque()
while tmt_start:
    q.append(tmt_start.pop())

max_x = x
max_y = y
bfs_checker = 0
while q:
    x, y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<= nx < max_x and 0<= ny < max_y and visited[nx][ny] == 0:
            if graph[nx][ny] == 0:
                visited[nx][ny] = visited[x][y] + 1
                bfs_checker = 1
                q.append([nx, ny])
                tmt_cnt += 1
                max = visited[nx][ny]

if tmt_total == tmt_cnt:
    if bfs_checker == 1:
        print(max - 1)
    else:
        print(0)
else:
    print(-1)
