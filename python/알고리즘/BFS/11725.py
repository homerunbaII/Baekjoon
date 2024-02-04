from collections import deque
import sys

input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n + 1)]
visited = [0 for _ in range(n + 1)]

for _ in range(n-1):
    p, c = map(int, input().split())
    graph[p].append(c)
    graph[c].append(p)

def bfs(start):
    q = deque()
    visited[start] = -1
    q.append(start)
    while q:
        x = q.popleft()
        for i in graph[x]:
            if visited[i] == 0:
                visited[i] = x
                q.append(i)
bfs(1)

for i in visited[2:]:
    print(i)

