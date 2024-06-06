from collections import deque
n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]
visited = [0 for _ in range(n + 1)]
for i in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited[1] = 1

q = deque([1])

while q:
    x = q.popleft()
    for nx in graph[x]:
        if visited[nx] == 0:
            q.append(nx)
            visited[nx] = 1

print(sum(visited) - 1)
