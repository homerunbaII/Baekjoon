
n, m = map(int, input().split())
tetris = [list(map(int, input().split())) for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]
result_list = [0]

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, level, value):
    if level == 3:
        if result_list[0] < value:
            result_list.pop()
            result_list.append(value)
        return
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0:
            if level == 1:
                visited[nx][ny] = 1
                dfs(x, y, level + 1, value + tetris[nx][ny])
                visited[nx][ny] = 0
            visited[nx][ny] = 1
            dfs(nx, ny, level + 1, value + tetris[nx][ny])
            visited[nx][ny] = 0

for i in range(n):
    for j in range(m):
        visited[i][j] = 1
        dfs(i, j, 0, tetris[i][j])
        visited[i][j] = 0

print(max(result_list))
