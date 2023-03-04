from collections import deque

que = deque([1, 2, 3, 4, 5, 6, 7, 8])

que.rotate(1)

print(list(que))
