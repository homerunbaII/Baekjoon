n = int(input())

arr = list(map(int, input().split()))

dp = [0 for _ in range(n)]

for i in range(n):
    if i == 0:
        dp[i] = arr[i]
    else:
        big = 0
        for j in range(i):
            if arr[i] > arr[j]:  # 현재보다 작은 수를 가진 원소들 中
                if dp[j] > big:
                    big = dp[j]
        dp[i] = big + arr[i]

print(max(dp))
