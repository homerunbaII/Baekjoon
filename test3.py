import sys

input = sys.stdin.readline

n = int(input())
meetlist = []

for i in range(n):
    meetlist.append(list(map(int, input().split())))

meetlist.sort(key=lambda x: (x[1], x[0]))
cnt = 1
endtime = meetlist[0][1]  # 4

for i in meetlist:
    if endtime <= i[0]:
        cnt += 1
        endtime = i[1]

print(cnt)
