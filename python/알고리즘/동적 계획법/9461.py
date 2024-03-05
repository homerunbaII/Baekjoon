dp = [0 for _ in range(101)]
dp[1], dp[2], dp[3], dp[4], dp[5] = 1, 1, 1, 2, 2
dp[6], dp[7], dp[8], dp[9], dp[10] = 3, 4, 5, 7, 9

for i in range(11, 101):
    dp[i] = dp[i-1] + dp[i-5]

for i in range(int(input())):
    n = int(input())
    print(dp[n])