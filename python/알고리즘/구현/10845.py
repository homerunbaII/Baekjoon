import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

q = deque()

for i in range(n):
    command = input().rstrip()
    if command[:4] == 'push':
        command, num = command.split()
    if command == 'push' :
        q.append(num)
    if command == 'pop':
        if len(q) != 0:
            print(q.popleft())
        else:
            print(-1)
    if command == 'size' :
        print(len(q))
    if command == 'empty' :
        if len(q) == 0:
            print(1)
        else:
            print(0)
    if command == 'front' :
        if len(q) != 0:
            print(q[0])
        else:
            print(-1)
    if command == 'back'  :
        if len(q) != 0:
            print(q[-1])
        else:
            print(-1)