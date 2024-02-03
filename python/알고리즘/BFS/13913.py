from collections import deque

def bfs(x,y):
    q = deque()
    q. append(x)
    while q: 
        x = q.popleft()
        if x == y:
            break
        for i in [x -1 ,x + 1, x * 2]:
            if 0<= i < 100001 and visited[i] == 0:
                visited[i] = visited[x] + 1
                visited_route[i] = x
                q.append(i)


    

start, end = map(int, input().split())
# 방문여부 = 시간, 이전 노드
visited = [0 for _ in range(100001)]
visited_route = [0 for _ in range(100001)]
visited[start] = 1

bfs(start, end)

print(visited[end] - 1)

route = []
current = end
while current != start:
    route.append(current)
    current = visited_route[current]
route.append(start)

print(*route[::-1])