from collections import deque

building, start, end, up, down = map(int, input().split())

visited = [0 for _ in range(building + 1)]
visited[0] = -1

def bfs(building, start, end, up, down):
    q = deque()
    dx = [up, -down]
    q.append(start)
    while q:
        x = q.popleft()
        for i in range(2):
            nx = x + dx[i]
            if 1 <= nx < building + 1 and visited[nx] == 0:
                visited[nx] = visited[x] + 1
                q.append(nx)

visited[start] = 1
bfs(building, start, end, up, down)

if visited[end] == 0:
    print('use the stairs')
else:
    print(visited[end] -1 )
