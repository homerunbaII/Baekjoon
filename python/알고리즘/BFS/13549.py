from collections import deque

def bfs(x):
    q = deque()
    q.append(x)
    dx = [-1, +1]
    while q:
        x = q.popleft()
        for i in range(2,-1,-1):
            if i < 2:
                nx = x + dx[i]
            else: 
                nx = x * 2
            if 0 <= nx < 100001:
                if visited[nx][1] == 0:
                        q.append(nx)
                        if i < 2:
                            visited[nx][0] = visited[x][0] + 1
                            visited[nx][1] = 1
                        else:
                            visited[nx][0] = visited[x][0]
                            visited[nx][1] = 1
                if visited[nx][1] == 1:
                    if i < 2:
                        if visited[nx][0] > visited[x][0] + 1:
                            visited[nx][0] = visited[x][0] + 1
                    else:
                        if visited[nx][0] > visited[x][0]:
                            visited[nx][0] = visited[x][0]

        

start, target = map(int, input().split())

# 시간, visited
visited = [[0,0] for _ in range(100001)]

visited[start][1] = 1
bfs(start)
print(visited[target][0])