n , target = map(int, input().split())

coin_list = []
dp = [10E9] * 10001
dp[0] = 0

for _ in range(n):
    coin = int(input())
    coin_list.append(coin)

coin_list = list(set(coin_list))
coin_list.sort()

for i in coin_list:
    n = i 
    while n <= 10000:
        if dp[n] > dp[n-i] + 1:
            dp[n] =  dp[n-i] + 1
        n += 1



if dp[target] == 10E9:
    print(-1)
else: 
    print(dp[target])