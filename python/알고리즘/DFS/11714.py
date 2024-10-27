from collections import deque

n,m = map(int, input().split())

graph = [[]for _ in range(n + 1)]
visited = [0 for _ in range(n + 1)]

for i in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)



def dfs(a):
    q = deque()
    for i in graph[a]:
        q.append(i)
    while q:
        y = q.popleft()
        if visited[y] == 0:
            visited[y] = 1
            dfs(y)


cnt = 0

for i in range(1, n + 1):
    if visited[i] == 0:
        cnt += 1
        dfs(i)
    
print(cnt)
