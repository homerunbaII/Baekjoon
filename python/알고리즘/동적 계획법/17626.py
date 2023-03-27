import math
import sys

n = int(sys.stdin.readline())
dp = [0] * (n + 1)
dp[1] = 1


for i in range(2, n+1):  # 2 3 4 5 6 7
    min_val = 1e9
    for j in range(1, 50001):  # 1, 2
        if j**2 > i:
            break
        min_val = min(min_val, dp[i - (j ** 2)])
    dp[i] = min_val + 1

print(dp[n])
