n, weight_max = map(int, input().split())

dp = [0] * (weight_max + 1)

items = []

for i in range(n):
    w, v = map(int, input().split())
    items.append([w, v])

for item in items:
    w, v = item
    visited = [0] * (weight_max + 1)
    for i in range(weight_max, -1, -1):
        if i + w <= weight_max :
            if dp[i + w] < dp[i] + v:
                dp[i + w] = dp[i] + v

print(dp)
print(max(dp))

    
