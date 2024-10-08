import sys

input = sys.stdin.readline

n, m = map(int, input().split())

vec = []

for i in range(n):
    vec.append(list(map(int, input().split())))

for x in range(n):
    for y in range(1, m):
        vec[x][y] = vec[x][y] + vec[x][y-1]

trial = int(input())

for i in range(trial):
    total = 0
    x1, y1, x2, y2 = map(int, input().split())
    for x in range(x1 - 1, x2): 
            if y > 1 :
                total += vec[x][y2 - 1] - vec[x][y1 - 2]
            else:
                total += vec[x][y2 - 1]
    print(total)
            

