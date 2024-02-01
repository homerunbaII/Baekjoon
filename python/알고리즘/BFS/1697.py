from collections import deque


def dfs(x,y):
    q= deque()
    dx = [-1, +1]
    q.append(x)
    while q:
        x = q.popleft()
        for i in range(3):
            if i < 2:
                nx = x + dx[i]
            elif i == 2:
                nx = x * 2
            if 0 <= nx < 100001:
                if visited[nx] == 0:
                    visited[nx] = visited[x] + 1
                    if nx == y:
                        break
                    q.append(nx)
        if nx == y:
            break



start, target = map(int, input().split())

visited = [0] * 100001
visited[start] = 1

dfs(start, target)


print(visited[target] - 1)


