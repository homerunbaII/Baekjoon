from collections import deque

def bfs(x, y) :
    dx = [-2, -1, 1, 2, -2, -1, 1, 2]
    dy = [-1, -2 ,-2 ,-1 ,1 ,2 ,2 ,1]
    q = deque()
    q.append([x,y])
    while q:
        x,y = q.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < length and 0 <= ny < length:
                print(nx, ny)
                if visited[nx][ny] == 0:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append([nx, ny])



    

for _ in range(int(input())):
    length = int(input())
    x ,y = map(int, input().split())
    visited = [[0] * (length) for _ in range(length) ]
    target_x, target_y = map(int, input().split())
    visited[x][y] = 1
    bfs(x, y)
    print(visited[target_x][target_y] - 1)
    print(visited)
