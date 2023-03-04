import sys
from collections import deque

n = int(input())

queue = deque([])

for i in range(n):
    command = sys.stdin.readline().split()
    if 'push' in command:
        queue.append(command[1])  # command[1]은 정수 x
    if command[0] == 'pop':
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    if command[0] == 'size':
        print(len(queue))
    if command[0] == 'empty':
        if not queue:
            print(1)
        else:
            print(0)
    if command[0] == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)
    if command[0] == 'back':
        if queue:
            print(queue[-1])
        else:
            print(-1)
