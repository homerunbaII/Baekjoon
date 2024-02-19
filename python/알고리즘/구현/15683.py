n , m = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(n)]
dx_u = [i for i in range(0, -n, -1)]
dx_d = [i for i in range(0, n)]
dy_l = [i for i in range(0, -m, -1)]
dy_r = [i for i in range(0, m)]
print(dx_u, dx_d, dy_l, dy_r)

def cctv(num,x,y):
    if num == 5:
        up(x,y)
        down(x,y)
        right(x,y)
        left(x,y)

    

def up(x,y):
    for i in range(n):
        nx = x + dx_u[i]
        if 0 <= nx < n:
            if room[nx][y] == 6:
                break
            else:
                room[nx][y] = -1
def down(x, y):
    for i in range(n):
        nx = x + dx_d[i]
        if 0 <= nx < n:
            if room[nx][y] == 6:
                break
            else:
                room[nx][y] = -1

def left(x, y):
    for i in range(n):
        ny = y + dy_l[i]
        if 0 <= ny < m:
            if room[x][ny] == 6:
                break
            else:
                room[x][ny] = -1

def right(x,y):
    for i in range(n):
        ny = y + dy_r[i]
        if 0 <= ny < m:
            if room[x][ny] == 6:
                break
            else:
                room[x][ny] = -1



# for x in range(n):
#     for y in range(m):
#         room[x][y]
cctv(5,1,3)
print(room)

