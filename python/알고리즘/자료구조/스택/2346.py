from collections import deque

n = int(input())

balloon = list(map(int, input().split()))

for i in range(n):
    balloon[i] = [balloon[i]]
    balloon[i].append(i+1)

balloon = deque(balloon)

for i in range(n):
    popnum = balloon.popleft()
    rotatenum = popnum[0]
    print(popnum[1], end=' ')
    if rotatenum >= 0:
        balloon.rotate(-(rotatenum - 1))
    else:
        balloon.rotate(-(rotatenum))
