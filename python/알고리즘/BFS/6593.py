from collections import deque
z, x, y = map(int, input().split())

def bfs(z,x,y, end_z, end_x, end_y,max_z,max_x,max_y):
    q = deque()
    q.append([z,x,y])
    dz = [0, 0, 0, 0, 1, -1]
    dx = [1, -1, 0, 0, 0, 0]
    dy = [0, 0, 1, -1, 0, 0]
    while q:
        if z == end_z and x == end_x and y == end_y:
            break
        z, x, y = q.popleft()
        for i in range(6):
            nz = z + dz[i]
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nz < max_z and 0<= nx < max_x and 0<= ny < max_y and visited[nz][nx][ny] == 0:       
                if graph[nz][nx][ny] == '.' or graph[nz][nx][ny] == 'E':
                    visited[nz][nx][ny] = visited[z][x][y] + 1
                    q.append([nz,nx,ny])
                    



while x or z or y:
    visited = [[[0 for _ in range(y)] for _ in range(x)] for _ in range(z)]
    graph = []
    for i in range(z):
        graph_z = []
        for j in range(x + 1):
            if j % (x+1) == x:
                input()
                continue
            else:
                a = list(input())
                for k in range(y):
                    if a[k] == 'S':
                        start_location_z = i
                        start_location_x = j
                        start_location_y = k
                        visited[i][j][k] = 1
                    if a[k] == 'E':
                        end_location_z = i
                        end_location_x = j
                        end_location_y = k
                graph_z.append(a)
        graph.append(graph_z)
    bfs(start_location_z,start_location_x,start_location_y,end_location_z,end_location_x,end_location_y,z,x,y)
    if visited[end_location_z][end_location_x][end_location_y] == 0:
        print("Trapped!")
    else:
        minute = visited[end_location_z][end_location_x][end_location_y] - 1
        print(f'Escaped in {minute} minute(s).')
    z, x, y = map(int, input().split())
    