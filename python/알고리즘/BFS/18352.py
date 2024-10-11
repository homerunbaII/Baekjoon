from collections import deque
import sys

input = sys.stdin.readline

city, road, distance, start = map(int, input().split())

city_list = []

graph = [[] for _ in range(city + 1)] # [[],[2,3],[3,4],[],[]]
visited = [0 for i in range(city + 1)] # [0,0,0,0,0]


for _ in range(road):
    x, y = map(int, input().split())
    graph[x].append(y)


def bfs(start):
    q = deque()
    q.append(start)
    while q:
        x = q.popleft()
        for i in graph[x]:
            if i != start:
                if visited[i] == 0 or visited[x] + 1 < visited[i]: 
                    visited[i] = visited[x] + 1
                    q.append(i)

bfs(start)

for i in range(len(visited)):
    if visited[i] == distance:
        city_list.append(i)

if city_list:
    for i in city_list:
        print(i)
else:
    print(-1)


