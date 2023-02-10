n = int(input())
cnt = n

num_list = list(map(int, input().split()))

for i in num_list:
    if (i == 1):
        cnt -= 1
    else:
        for j in range(2, i):
            if (i % j == 0):
                cnt -= 1
                break

print(cnt)
