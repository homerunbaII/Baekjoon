# 1. 비어있는 칸 -> 좋아하는 학생이 주변에 가장 많은 칸으로
# 2. 1이 여러개면, 주변 칸 중 비어있는 칸이 가장 많은 칸
# 3. 2가 여러개면, 행의 번호가 가장 작은, 그것도 같으면 열의 번호
import sys

imput = sys.stdin.readline

n = int(input())
visited = [[0 for _ in range(n)] for _ in range(n)]

order_list = []
f_dictionary = {}

for i in range(n**2):
    a= list(map(int, input().split()))
    order_list.append(a)
    f_dictionary[a[0]] = a[1:]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def repalce_seet(student):
    favorite_empty_degree = []
    for x in range(n):
        for y in range(n):
            ## 비어있는 칸
            if visited[x][y] == 0:
                f_cnt = 0
                e_cnt = 0 
                #상하좌우 탐색
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    ## 범위를 벗어나지 않는다면
                    if 0 <= nx < n and 0 <= ny < n:
                        # 좋아하는 학생 수
                        if visited[nx][ny] in f_dictionary[student]:
                            f_cnt += 1
                        # 비어있는 칸 수
                        if visited[nx][ny] == 0:
                            e_cnt += 1                   
                        # 정보 저장               
                    favorite_empty_degree.append([f_cnt, e_cnt, x, y])
    favorite_empty_degree.sort(key = lambda x : (-x[0], -x[1], x[2],x[3]))
    f_cnt, e_cnt, x, y = favorite_empty_degree[0]
    visited[x][y] = student
    return



for i in order_list:
    student = i[0]
    repalce_seet(student)

satisfied_total = 0
satisfied_degree = [0,1,10,100,1000]

for x in range(n):
    for y in range(n):
        s_cnt = 0
        #상하좌우 탐색
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            ## 범위를 벗어나지 않는다면
            if 0<= nx < n and 0<=ny<n:
                if visited[nx][ny] in f_dictionary[visited[x][y]]:
                    s_cnt += 1
        satisfied_total += satisfied_degree[s_cnt]

print(satisfied_total)
