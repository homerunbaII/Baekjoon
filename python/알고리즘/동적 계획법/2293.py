n, target = map(int, input().split())

money_bag = []
for i in range(n):
    money_bag.append(int(input()))

dp = [0 for _ in range(target + 1)]
dp[0] = 1

for i in money_bag:
    for j in range(i, target + 1):
        dp[j] += dp[j - i]

print(dp[target])