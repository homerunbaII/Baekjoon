from collections import deque
def bfs(x,y):
    dx = [0 ,0, 1, -1]
    dy = [1, -1, 0, 0]
    q = deque()
    q.append([x,y])
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if visited[nx][ny] == 0 and graph[nx][ny] == 1:
                    visited[nx][ny] = 1
                    q.append([nx,ny])
            

        






for _ in range(int(input())):
    m , n, k = map(int, input().split())
    visited = [[0 for _ in range(m) ] for _ in range(n)]
    graph  = [[0 for _ in range(m) ] for _ in range(n)]
    bfs_list = []
    for i in range(k):
        y,x = map(int, input().split())
        graph[x][y] = 1
        bfs_list.append([x,y])
    bfs_list = sorted(bfs_list, key = lambda x : x[0])
    count = 0
    for i in bfs_list:
        x ,y = i[0], i[1]
        if visited[x][y] == 0:
            bfs(x, y)
            count += 1
    print(count)
    

    
