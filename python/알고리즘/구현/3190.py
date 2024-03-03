def head(nx, ny, d, direction):
    if direction == 0:
        q.appendleft([nx, ny, 1, d])
    else:
        # 방향에 따라 변형
        if direction == 'D':
            q.appendleft([nx, ny, 1, (d + 1) % 4])
            turn_graph[nx][ny] = 'D'
        if direction == 'L':
            q.appendleft([nx, ny, 1, (d - 1) % 4])
            turn_graph[nx][ny] = 'L'

def head_2(nx, ny, d, direction, inf):
    if direction == 0:
        q.append([nx, ny, inf, d])
    else:
        # 방향에 따라 변형
        if direction == 'D':
            q.append([nx, ny, inf, (d + 1) % 4])
            turn_graph[nx][ny] = 'D'
        if direction == 'L':
            q.append([nx, ny, inf, (d - 1) % 4])
            turn_graph[nx][ny] = 'L'
        if inf == 2:
                    if turn_graph[nx][ny] != 0:
                        turn_graph[nx][ny] = 0

from collections import deque
import sys

input = sys.stdin.readline

# 보드의 크기
n = int(input())

graph = [[0 for _ in range(n)] for _ in range(n)]
turn_graph = [[0 for _ in range(n)] for _ in range(n)]

# 사과의 개수
k = int(input())

# 사과 위치
for i in range(k):
    x, y = map(int, input().split())
    # 사과 위치 인덱스로 만들기
    x, y = x - 1, y - 1
    graph[x][y] = -1

# 방향 전환 횟수
l = int(input())

direction_dic = {}

for i in range(l):
    x, d = input().split()
    x = int(x)
    direction_dic[x] = d

# 우 하 좌 상
dx = [0,1,0,-1]
dy = [1,0,-1,0]

# 죽음
die = 0

# 시간
tm = 0

# 처음 머리(꼬리)
graph[0][0] = 1
q = deque()
# x, y, 몸정보, 방향
q.append([0,0,2,0])

while True:
    tm += 1
    direction = 0

    if tm in direction_dic:
        # 방향 갱신
        direction = direction_dic[tm]

    # 머리 검사
    x, y, inf, d = q.popleft()
    nx = x + dx[d]
    ny = y + dy[d]
    if 0 <= nx < n and 0 <= ny < n and (graph[nx][ny] == -1 or graph[nx][ny] == 0):
        # 사과일 때
        if graph[nx][ny] == -1:
            # 사과 = 머리
            graph[nx][ny] = 1
            q.appendleft([x, y, inf, d])
            # 머리 증식
            head(nx, ny, d, direction)
            continue
        # 사과가 아닐 때
        else:
            graph[nx][ny] = 1
            head_2(nx, ny, d, direction, inf)
            graph[x][y] = 0
            a = len(q) - 1
            for i in range(a):
                x, y, inf, d = q.popleft()
                nx = x + dx[d]
                ny = y + dy[d]
                graph[nx][ny] = 1
                graph[x][y] = 0
                if turn_graph[nx][ny] == 0:
                    q.append([nx,ny,inf,d])
                else:
                    if turn_graph[nx][ny] == 'D':
                        q.append([nx, ny, inf, (d + 1) % 4])
                    if turn_graph[nx][ny] == 'L':
                        q.append([nx, ny, inf, (d - 1) % 4])
                if inf == 2:
                    if turn_graph[nx][ny] != 0:
                        turn_graph[nx][ny] = 0
    else: 
        # 죽음
        die = 1
    if die == 1:
        break

print(tm) 



