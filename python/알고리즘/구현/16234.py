from collections import deque

n , small ,big = map(int, input().split())

graph = [list(map(int,input().split())) for _ in range(n)]


dx = [1, -1, 0 ,0]
dy = [0, 0, -1, 1]

def check_near(x,y):
    union = []
    q = deque()
    first = [x,y]
    q.append([x,y])
    while q:
        x,y = q.popleft()
        here = graph[x][y]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx < n and 0 <= ny < n:
                if visited[nx][ny] == 0:
                    there = graph[nx][ny]
                    diff = abs(here - there)
                    if small <= diff <= big:
                        visited[nx][ny] = 1
                        union.append([nx,ny])
                        q.append([nx,ny])
    return union

trial = 0

while True:
    visited = [[0 for _ in range(n)] for _ in range(n)]
    union_list = []
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                lst = check_near(i,j)
                if len(lst) != 0:
                    union_list.append(lst)
    if len(union_list) == 0:
        break
    trial += 1
    while union_list:
        unioned = union_list.pop()
        union_total = 0
        union_cnt = 0
        for i in unioned:
            x, y = i
            union_total += graph[x][y]
        new_union = union_total // len(unioned)
        for i in unioned:
            x,y = i
            graph[x][y] = new_union

print(trial)           
