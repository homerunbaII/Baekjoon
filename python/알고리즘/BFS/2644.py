from collections import deque

def dfs(node) : 
    q = deque()
    q.append(node)
    while q:
        node = q.popleft()
        for n in graph[node]:
            if visited[n] == 0:
                visited[n] = visited[node] + 1
                q.append(n)


n = int(input())
graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
man_1, man_2 = map(int, input().split())

relation = int(input())
for i in range(relation):
    parent, kid = map(int, input().split())
    graph[parent].append(kid)
    graph[kid].append(parent)

dfs(man_1)

if visited[man_2] == 0 :
    print(-1)
else:
    print(visited[man_2])
