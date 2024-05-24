from collections import deque

n = int(input())

graph = [[0 for _ in range(n)] for _ in range(n)]
visited = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    a = input()
    for j in range(n):
        graph[i][j] = int(a[j])


dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
ans = []

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and visited[i][j] == 0 :
            cnt = 1
            visited[i][j] = 1
            q = deque()
            q.append([i,j])
            while q:
                x,y = q.popleft()
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if 0 <= nx < n and 0 <= ny < n:
                        if visited[nx][ny] == 0 and graph[nx][ny] == 1:
                            visited[nx][ny] = 1
                            q.append([nx,ny])
                            cnt += 1
            ans.append(cnt)



ans.sort()

print(len(ans))
for i in ans:
    print(i)
            