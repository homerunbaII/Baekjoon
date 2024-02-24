n , m = map(int, input().split())

tetris =[list(map(int, input().split())) for _ in range(n)]
result = [[0 for _ in range(m)] for _ in range(n)]


dx = [1, -1, 0, 0]
dy = [0 ,0, -1, 1]

def dfs(x,y, level, value):
    if level == 3:
        result_list.append([value, x, y])
        return
    else:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx < n and 0<= ny < m and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    level += 1
                    print(nx,ny,level,'snxnylevel')
                    dfs(nx, ny, level, value + tetris[nx][ny])
                    visited[nx][ny] = 0
                    level -= 1
                    print(nx,ny,level,'fnxnylevel')
    
for i in range(n):
    for j in range(m):
        visited = [[0 for _ in range(m)] for _ in range(n)]
        visited[i][j] = 1
        result_list = []
        level = 0
        value = tetris[i][j]
        lst = []
        dfs(i,j,level, value)
        break
print(result_list)