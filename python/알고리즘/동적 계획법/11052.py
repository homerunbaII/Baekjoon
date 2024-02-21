n = int(input())
pack = list(map(int, input().split()))
dp = [0] * (n+1)
card = [0] *(n+1)
for i in range(n):
    card[i + 1] = pack[i]

for i in range(1, n+1):
    card_now = card[i]
    for j in range(i, n + 1):
        if dp[j] < dp[j - i] + card_now:
            dp[j] = dp[j - i] + card_now

print(dp[n])