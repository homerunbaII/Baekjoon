n = int(input())
num_list = list(map(int, input().split()))

num_list = num_list[:: -1]

## 10 20 20 10 30 10 자기보다 작은 수들 중의 dp[max]
dp = [1 for _ in range(n)] 

print(num_list)
for i in range(n):
    for j in range(0, i):
        if num_list[i] > num_list[j]:
            if dp[j] >= dp[i]:
                dp[i] = dp[j] + 1

print(max(dp))
