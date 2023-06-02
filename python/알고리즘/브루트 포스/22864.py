a, b, c, m = map(int, input().split())

tired = 0
work_cnt = 0

for i in range(24):
    if tired <= m - a:
        tired += a
        work_cnt += b
    else:
        tired -= c
    if tired < 0:
        tired = 0

print(work_cnt)
