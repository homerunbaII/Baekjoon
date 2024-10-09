x, y , time = map(int,input().split())
vec = []
field = [[0 for i in range(y)] for _ in range(x)]

for _ in range(x):
    vec.append(input())


# 폭탄 시간으로 변환 
for i in range(x):
    for j in range(y):
        if vec[i][j] == '.':
            pass
        else:
            field[i][j] += 2

time -= 1
cnt = 0

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

while time:
    # 폭탄 시간 감소
    for i in range(x):
        for j in range(y):
            if field[i][j] == 3 or field[i][j] == 2:
                field[i][j] -= 1
            elif field [i][j] == 1:
                field[i][j] = 0
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0 <= nx < x and 0 <= ny < y:
                        if field[nx][ny] == 1:
                            pass
                        else:
                            field[nx][ny] = 0
            else:
                pass
    # 2초에 1번씩 폭탄 설치
    if cnt % 2 == 0:
        for i in range(x):
            for j in range(y):
                if field[i][j] == 0:
                    field[i][j] = 3
    cnt += 1
    time -= 1 

for i in range(x):
    for j in range(y):
        if field[i][j] == 0:
            print('.', end = '')
        else:
            print('O', end = '')
    print()


