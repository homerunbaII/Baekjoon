a, b = map(int, input().split())

cnt = 0

for i in range(a + 1):
    if i < 10:
        i = '0' + str(i)
    for j in range(60):
        if j < 10:
            j = '0' + str(j)
        for p in range(60):
            if p < 10:
                p = '0' + str(p)
            if str(b) in str(i) or str(b) in str(j) or (str(b) in str(p)):
                cnt += 1

print(cnt)
