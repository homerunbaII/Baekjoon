n, m, r = map(int, input().split())

arr = []

for _ in range(n):
    arr.append(list(map(int, input().split())))

for k in range(r):
    s = min(n, m) // 2
    for j in range(s):
        x, y = j, j
        pre = arr[x][y]
        for i in range(x + 1, n - j):
            tmp = arr[i][j]
            arr[i][j] = pre
            pre = tmp
        for i in range(y+1, m - j):
            tmp = arr[n - 1 - j][i]
            arr[n - 1 - j][i] = pre
            pre = tmp
        for i in range(n-j-2, j - 1, -1):
            tmp = arr[i][m-1-j]
            arr[i][m-1-j] = pre
            pre = tmp
        for i in range(m-2-j, j-1, -1):
            tmp = arr[j][i]
            arr[j][i] = pre
            pre = tmp

for i in range(n):
    for j in range(m):
        print(arr[i][j], end=' ')
    print()
