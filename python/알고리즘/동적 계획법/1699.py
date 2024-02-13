import math

n = int(input())

dp = [10000] * 100001
dp[0] = 0
square_list = []

for i in range(1, 100001):
    temp = int(math.sqrt(i))
    if temp ** 2 == i:
        square_list.append(i)

# for i in square_list:
#     dp[i] = dp[i] + dp[i-1]

for i in range(1, 100001):
    for j in square_list:
        if j  <= i:
            if dp[i] > dp[i - j] + 1 :
                dp[i] = dp[i - j] + 1
print(dp[n])
