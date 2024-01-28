from collections import deque

def dfs(v):
    visited[v] = True
    print(v, end = ' ')
    for i in graph[v]:
        if visited[i] == False:
            dfs(i)


def bfs(v) :
    q = deque()
    q.append(v)
    visited[v] = True
    while q:
        v = q.popleft() # v = 1
        print(v, end = " ")
        for i in graph[v]:
            if visited[i] == False:
                visited[i] = True
                q.append(i)

n, m, v = map(int, input().split())

graph = [[] for _ in range(n + 1)]


for _ in range(m):
    a ,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort()

## dfs
visited = [False] * (n + 1)
dfs(v)
print()
## bfs
visited = [False] * (n + 1)
bfs(v)

