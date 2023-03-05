from collections import deque

que = deque([])

n = int(input())

for i in range(n):
    order = input().split()
    if order[0] == 'push_front':
        que.appendleft(order[1])
    if order[0] == 'push_back':
        que.append(order[1])
    if order[0] == 'pop_front':
        if que:
            print(que.popleft())
        else:
            print(-1)
    if order[0] == 'pop_back':
        if que:
            print(que.pop())
        else:
            print(-1)
    if order[0] == 'size':
        print(len(que))
    if order[0] == 'empty':
        if que:
            print(0)
        else:
            print(1)
    if order[0] == 'front':
        if que:
            print(que[0])
        else:
            print(-1)
    if order[0] == 'back':
        if que:
            print(que[-1])
        else:
            print(-1)
