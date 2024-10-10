import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

mapp = []
visited = [[0 for _ in range(m)] for _ in range(n)]


for i in range(n):
    mapp.append(list(map(int, input().split())))

for i in range(n):
    for j in range(m):
        if mapp[i][j] == 2:
            start = [i,j]

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(start_x, start_y):
    q = deque()
    q.append([start_x, start_y])

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx < n and 0<= ny < m:
                if mapp[nx][ny] == 1 and visited[nx][ny] == 0:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append([nx,ny])

bfs(start[0], start[1])

for i in range(n):
    for j in range(m):
        if mapp[i][j] == 1 and visited[i][j] == 0:
            visited[i][j] = -1


for i in visited:
    print(*i)