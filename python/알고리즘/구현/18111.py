import sys

input = sys.stdin.readline

n, m ,b = map(int, input().split())
mine = []

for _ in range(n):
    ground =list(map(int, input().split()))
    for i in ground:
        mine.append(i)

maxi = (sum(mine) + b) // (n*m)
min_time = 10e9
ground_h = 0

# i = 목표, h = 현재
for i in range(maxi , min(mine) - 1, -1):
    time = 0
    for h in mine:
        if h - i >= 0:
            time += (h - i) * 2
        else:
            time += (i - h)
    if time < min_time :
        min_time = time
        ground_h = i
print(min_time, ground_h)
