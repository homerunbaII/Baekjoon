n  = int(input())

n_list = list(map(int, input().split()))

dp = [1 for _ in range(n)]
dp_2 = [1 for _ in range(n)]
for i in range(n):
    large = 0
    for j in range(i):
        # 기준 수보다 리스트 내의 숫자가 작다면
        if n_list[i] > n_list[j]:
            large = max(large, dp[j])
        dp[i] = large + 1

for i in range(n-1, -1, -1):
    large = 0
    for j in range(n-1, i, -1):
        if n_list[i] > n_list[j]:
            large = max(large, dp_2[j])
        dp_2[i] = large + 1

result = 0
for i in range(n):
    result = max(result, dp[i] + dp_2[i])
    

print(result - 1)