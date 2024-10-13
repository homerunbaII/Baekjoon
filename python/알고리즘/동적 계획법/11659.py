n , m = map(int, input().split())
num = list(map(int, input().split()))


dp = [0 for _ in range(n + 1)]

total = 0

for i in range(n):
    total += num[i]
    dp[i + 1] = total


for i in range(m):
    x, y = map(int, input().split())
    print(dp[y] - dp[x-1])


