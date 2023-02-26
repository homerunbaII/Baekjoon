import sys

input = sys.stdin.readline

n = int(input())
dlist = []
for i in range(n):
    dlist.append(list(map(int, input().split())))

for i in range(len(dlist)):  # 0123456
    cnt = 1
    for j in range(len(dlist)):  # 0123456
        if (dlist[i][0] < dlist[j][0] and dlist[i][1] < dlist[j][1]):
            cnt += 1
    print(cnt, end='')
