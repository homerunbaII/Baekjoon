from collections import deque

n , m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
bacon_map = []

# graph 지도 만들기
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)


def bfs(start):
    visited = [0 for _ in range(n + 1)]
    q = deque()
    q.append(start)

    while q:
        x = q.popleft()
        for i in graph[x]:
            if i != start:
                if visited[i] == 0 or visited[x] + 1 < visited[i]:
                    visited[i] = visited[x] + 1
                    q.append(i)

    bacon_map.append(sum(visited))
    
for i in range(1, n + 1):
    bfs(i)

small = min(bacon_map)

for i in range(m):
    if bacon_map[i] == small:
        print(i + 1)
        break
