from collections import deque
import sys

def bfs(start):
    visited = [-1 for _ in range(n + 1)]
    visited[start] = 0
    q = deque()
    q.append(start)

    while q:
        temp = q.popleft()
        for child, weight in tree[temp]:
            if visited[child] == -1:
                visited[child] = visited[temp] + weight
                q.append(child)
    m = max(visited)
    return [visited.index(m),m]

input = sys.stdin.readline

n = int(input())

tree = [[]for _ in range(n + 1)]



for _ in range(n - 1):
    m , n , w = map(int, input().split())
    tree[m].append([n,w])
    tree[n].append([m,w])

if n == 1:
    print(0)
else:
    print(bfs(bfs(1)[0])[1])
        


