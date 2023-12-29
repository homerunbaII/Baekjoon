cnt = 0



for i in range(11):
    lists = list(map(int, input().split()))
    for j in lists:
        if j == 0:
            cnt += 1
print(cnt)