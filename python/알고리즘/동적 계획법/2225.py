import math

n , k  = map(int,input().split())

dp = [[1], [1,1]]

for i in range(3, n + 1):
    lst = [1 for _ in range(i)]
    for j in range(1, i - 1):
        lst[j] = dp[i - 2][j -1] + dp[i - 2][j]
    dp.append(lst)

result = 0


for i in range(k):
    if i > n - 1:
        break
    else:
        result += math.comb(k ,i + 1) * dp[n-1][i] 

print(result% 1000000000)

