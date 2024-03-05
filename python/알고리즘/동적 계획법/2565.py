n = int(input())

elec = []

dp = [1] * (n)

for _ in range(n):
    start, end = map(int, input().split())
    elec.append([start, end])

elec.sort(key = lambda x : x[0])

for i in range(n):
    for j in range(i):
        if elec[i][1] > elec[j][1]:
            dp[i] = max(dp[j] + 1, dp[i])


print(n - max(dp))