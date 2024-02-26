def clean_dust_up():
    x, y = air_clean[0]
    # 청청기 윗칸 처리
    x = x-1
    graph[x][y] = 0

    while x > 0:
        graph[x][y] = graph[x - 1][y]
        x -= 1
    y = y + 1

    while y < m:
        graph[x][y - 1] = graph[x][y]
        y += 1
    y = y - 1

    while x < air_clean[0][0]:
        graph[x][y] = graph[x + 1][y]
        x += 1

    while y > 1:
        graph[x][y] = graph[x][y-1]
        y -= 1
    graph[x][y] = 0
def clean_dust_down():
    x, y = air_clean[1]
    x = x + 1
    graph[x][y] = 0

    while x < n - 1 :
        graph[x][y] = graph[x + 1][y]
        x = x + 1
    y = y + 1

    while y < m:
        graph[x][y - 1] = graph[x][y]
        y += 1
    y = y - 1

    while x > air_clean[1][0]:
        graph[x][y] = graph[x - 1][y]
        x -= 1

    while y > 1:
        graph[x][y] = graph[x][y-1]
        y -= 1
    graph[x][y] = 0


__name__ 

n , m, t = map(int, input().split())
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
graph =[list(map(int, input().split())) for _ in range(n)]

for i in range(t):
    air_clean = []
    dust_location = []
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                continue
            if graph[i][j] == -1:
                air_clean.append([i, j])
            else:
                dust_location.append([i, j, graph[i][j]])

    while dust_location:
        x, y, dust = dust_location.pop()
        # 확산 카운트
        cnt = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx < n and 0 <= ny < m:
                if graph[nx][ny] != -1:
                    graph[nx][ny] += (dust // 5)
                    cnt += 1
        graph[x][y] -= (dust // 5) * cnt

    clean_dust_up()
    clean_dust_down()

dust_cnt = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == -1:
            continue
        else:
            dust_cnt += graph[i][j]

print(dust_cnt)

    




