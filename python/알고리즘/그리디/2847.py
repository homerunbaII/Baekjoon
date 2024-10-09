import sys

input = sys.stdin.readline


n = int(input())
cnt = 0

level = []

for _ in range(n):
    point = int(input())
    level.append(point)

for i in range(n - 1, 0, -1):
    if level[i] > level[i-1]:
        continue
    else:
        cnt += (level[i-1] - level[i] + 1)
        level[i - 1] = level[i] - 1


print(cnt)