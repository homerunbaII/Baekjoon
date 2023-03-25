import sys
input = sys.stdin.readline

n = int(input())

mine_list = [list(input().rstrip()) for _ in range(n)]  # ...**..*
check_list = [list(input().rstrip()) for _ in range(n)]  # xxx.....

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

flag = False

for i in range(n):
    for j in range(n):
        if check_list[i][j] == 'x':
            if mine_list[i][j] == '*':
                flag = True
                continue
            cnt = 0
            for k in range(8):
                if 0 <= i + dx[k] < n and 0 <= j + dy[k] < n and mine_list[i+dx[k]][j+dy[k]] == '*':
                    cnt += 1
            check_list[i][j] = str(cnt)

if flag:
    for i in range(n):
        for j in range(n):
            if mine_list[i][j] == '*':
                check_list[i][j] = '*'

for i in check_list:
    print(''.join(i))
