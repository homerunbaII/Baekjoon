import sys
from collections import deque
start, target= map(int, sys.stdin.readline().split())
queue = deque()
queue.append(start)
visited = [0]*100001 # 최대 크기
cnt, result = 0,0
d_cnt = 0
while queue:
    d_cnt += 1
    x =  queue.popleft()
    temp = visited[x]
    if x == target: # 둘이 만났을 때
        result = temp # 결과
        cnt += 1 # 방문 횟수 +1
        continue
    
    for i in [x-1, x+1, x*2]:
        if 0 <= i < 100001:
            if visited[i] == 0:
                visited[i] = visited[x] + 1
                queue.append(i)
            elif visited[i]== visited[x] +1: #범위 안에있고 방문하지 않았거나, 다음 방문이 이전 방문+1이면
                queue.append(i) 
print(result)
print(d_cnt)
