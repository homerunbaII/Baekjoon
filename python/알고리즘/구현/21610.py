import sys
input = sys.stdin.readline

n, trial = map(int,input().split())

water = [list(map(int, input().split())) for _ in range(n)]
cloud_loc = [[0 for _ in range(n)] for _ in range(n)]

# 첫 구름 생성
cloud_loc[n - 1][0], cloud_loc[n - 1][1], cloud_loc[n - 2][0], cloud_loc[n - 2][1] = 1,1,1,1

#     ←,  ↖, ↑,  ↗,  →, ↘, ↓, ↙ 
dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

# 이동시에는 경계를 넘나들 수 있음



## 방향 꼭 -1 해서 주기!!!!!!!!!!!!
def cloud_move(direction, distance):
    distance = distance % n
    cloud_now = []
    # 구름 다음 위치 초기화
    for i in range(n):
        for j in range(n):
            if cloud_loc[i][j] == 1:
                # 현재 위치 확보
                cloud_now.append([i,j])
    new_cloud_loc = []
    for i in cloud_now:
        x, y = i[0] ,i[1]
        nx = x + (dx[direction] * distance)
        nx = nx % n
        ny = y + (dy[direction] * distance)
        ny = ny % n
        new_cloud_loc.append([nx, ny])
    return new_cloud_loc

for _ in range(trial):
    direction, distance = map(int, input().split())
    direction -= 1
    ## 구름 이동
    new_cloud_loc = cloud_move(direction, distance)
    cloud_loc = [[0 for _ in range(n)] for _ in range(n)]
    ## 이동된 위치에 비 1씩 증가                                            주의 나중에 구름이 사라진 칸이 아닌 곳에서 구름이 생겨야 함
    for new in new_cloud_loc:
        x,y = new
        water[x][y] += 1
    ## 복사 버그
    for copy_bug in new_cloud_loc:
        x, y = copy_bug
        for i in range(1,8,2):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if water[nx][ny] >= 1:
                    water[x][y] += 1
    ### 새로운 구름
    cloud_loc = [[0 for _ in range(n)] for _ in range(n)]
    
    before_cloud_temp = []
    for before in new_cloud_loc:
        x,y = before
        before_cloud_temp.append([x, y, water[x][y]])
        water[x][y] = 0
    for i in range(n):
        for j in range(n):
            if water[i][j] >= 2:
                water[i][j] -= 2
                cloud_loc[i][j] = 1     
    for i in range(len(before_cloud_temp)):
        x , y, value = before_cloud_temp[i]
        water[x][y] = value
    


total_water = 0
for i in water:
    total_water += sum(i)

print(total_water)