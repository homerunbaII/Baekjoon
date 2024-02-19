n = int(input())


dp_1 = [0] * n
dp_1[2] = 2
dp_1[3] = 3
dp_2 = [0] * n
for i in range(4,n):
    dp_1[i] = dp_1[i-1] + dp_1[i-2]

print(dp_1)