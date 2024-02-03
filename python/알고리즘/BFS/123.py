from collections import deque

def bfs(start, end):
    q = deque([start])
    visited[start] = 1  # 시작점을 방문 처리 (시간을 1부터 시작하여 계산)
    
    while q:
        x = q.popleft()
        if x == end:
            break
        for i in [x - 1, x + 1, x * 2]:
            if 0 <= i < 100001 and visited[i] == 0:
                visited[i] = visited[x] + 1
                visited_route[i] = x
                q.append(i)

# 입력 받기
start, end = map(int, input().split())

# 방문여부 및 이전 노드 기록
visited = [0 for _ in range(100001)]
visited_route = [0 for _ in range(100001)]

# BFS 실행
bfs(start, end)

# 결과 출력
print(visited[end] - 1)  # 시작점에서의 방문을 1로 시작했으므로 실제 단계 수는 -1

# 경로 추적
route = []
current = end
while current != start:
    route.append(current)
    current = visited_route[current]
route.append(start)

print(*route[::-1])
