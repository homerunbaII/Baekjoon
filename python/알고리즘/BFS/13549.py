# from collections import deque

# def bfs(x):
#     q = deque()
#     q.append(x)
#     dx = [-1, +1]
#     while q:
#         x = q.popleft()
#         for i in range(2,-1,-1):
#             if i < 2:
#                 nx = x + dx[i]
#             else: 
#                 nx = x * 2
#             if 0 <= nx < 100001:
#                 # 방문하지 않았던 점
#                 if visited[nx][1] == 0:
#                         q.append(nx)
#                         # 지금 최소 시간을 넣어준다
#                         if i < 2:
#                             visited[nx][0] = visited[x][0] + 1
#                             visited[nx][1] = 1
#                         else:
#                             visited[nx][0] = visited[x][0]
#                             visited[nx][1] = 1
#                 # 방문했던 점
#                 if visited[nx][1] == 1:
#                     # 새로운 시간이 더 짧은 경우 그 케이스를 넣어준다
#                     if i < 2:
#                         if visited[nx][0] > visited[x][0] + 1:
#                             visited[nx][0] = visited[x][0] + 1
#                     else:
#                         if visited[nx][0] > visited[x][0]:
#                             visited[nx][0] = visited[x][0]

        

# start, target = map(int, input().split())

# # 시간, visited
# visited = [[0,0] for _ in range(100001)]

# visited[start][1] = 1
# bfs(start)
# print(visited[target][0])
from collections import deque


def bfs(x,y):
    q = deque()
    q. append(x)
    while q:
        x = q.popleft()
        if x == y:
            break
        for i in  [x*2, x -1, x + 1]:
            if 0 <= i < 100001 and visited[i] == -1:
                q.append(i)
                if i == x*2:
                    visited[i] = visited[x]
                else:
                    visited[i] = visited[x] + 1

start, target = map(int, input().split())

visited = [-1 for _ in range(100001)]
visited[start] = 0
bfs(start, target)
print(visited[target])