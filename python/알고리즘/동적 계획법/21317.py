n = int(input())

dp = [0 for _ in range(n+1)]
jump = [[0, 0]]
energy_max = 0

for i in range(n - 1):
    e = list(map(int, input().split()))  # 1 2, 2 3, 4 5
    jump.append(e)

gj = int(input())


for i in range(2, n + 1):
    if i == 2:
        dp[i] = jump[1][0]
    else:
        dp[i] = min(dp[i - 1] + jump[i - 1][0], dp[i - 2] +
                    jump[i - 2][1])  # 먼저 작은 점프 큰 점프로만 dp를 구한다


for i in range(4, n+1):
    energy = dp[i] - dp[i - 3]
    if energy > energy_max:
        energy_max = energy
        flag = i


if energy_max > gj:
    dp[flag] = dp[flag - 3] + gj
    for i in range(flag + 1, n + 1):
        if i == flag + 1:
            dp[i] = dp[flag] + jump[i-1][0]
        else:
            dp[i] = min(dp[i - 1] + jump[i - 1][0], dp[i - 2] +
                        jump[i - 2][1])  # 먼저 작은 점프 큰 점프로만 dp를 구한다

print(dp[n])
