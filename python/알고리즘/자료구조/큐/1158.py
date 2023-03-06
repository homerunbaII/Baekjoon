from collections import deque

n, k = map(int, input().split())

result = []
que = deque(i for i in range(1, n + 1))

while (que):
    que.rotate(-(k-1))
    result.append(que.popleft())

print("<" + str(result)[1:-1] + ">")
