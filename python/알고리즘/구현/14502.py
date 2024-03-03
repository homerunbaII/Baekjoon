from itertools import combinations
from collections import deque

n, m =  map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]

def bfs(p_lst):
    new_graph = [a[:] for a in graph]
    new_virus_location = deque([a[:] for a in virus_location])
    result = 0
    for i in p_lst:
        x, y =  empty_location[i]
        new_graph[x][y] = 1
    while new_virus_location:
        q = deque()
        q.append(new_virus_location.popleft())
        while q:
            x, y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0<= nx < n and 0 <= ny < m:
                    if new_graph[nx][ny] == 0:
                        new_graph[nx][ny] = 2
                        q.append([nx,ny])
    for x in range(n):
        for y in range(m):
            if new_graph[x][y] == 0:
                result += 1
    return result

dx = [1, -1, 0, 0]
dy = [0, 0, -1 ,1]

empty_location = []
virus_location = []

for x in range(n):
    for y in range(m):
        if graph[x][y] == 0:
            empty_location.append([x,y])
        if graph[x][y] == 2:
            virus_location.append([x,y])

num_list = [i for i in range(len(empty_location))]
p = list(combinations(num_list, 3))
safe_zone = []

for i in p:
    safe_zone.append(bfs(i))

print(max(safe_zone))