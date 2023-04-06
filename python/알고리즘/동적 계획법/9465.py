t = int(input())

for i in range(t):
    n = int(input())
    dp1 = list(map(int, input().split()))
    dp2 = list(map(int, input().split()))
    for j in range(1, n):
        if j == 1:
            dp1[j] += dp2[j-1]
            dp2[j] += dp1[j-1]
        else:
            dp1[j] += max(dp2[j-1], dp2[j-2])
            dp2[j] += max(dp1[j-1], dp1[j-2])
    print(dp1, dp2)
    print(max(dp1[n-1], dp2[n-1]))
