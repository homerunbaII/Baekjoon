n, m = map(int, input().split())

arr = list(map(int, input().split()))
maximum = 0

for i in range(n-2):
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            temp = arr[i] + arr[j] + arr[k]
            if temp > m:
                temp = 0
            if temp > maximum:
                maximum = temp


print(maximum)
