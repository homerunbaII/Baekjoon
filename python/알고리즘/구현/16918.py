x, y , time = map(int,input().split())
vec = []
field = [[0 for i in range(y)] for _ in range(x)]

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(x):
    vec.append(input())

for i in range(x):
    for j in range(y):
        if vec[i][j] == '.':
            pass
        else:
            field[i][j] += 2

time -= 1

cnt = 0
while time:
    print(field, time)
    # 설치

    for i in range(x):
        for j in range(y):
            if field[i][j] == 3 or field[i][j] == 2:
                field[i][j] -= 1
            # 폭탄이 1
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
            # 폭탄이 0
            else:
                pass
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


