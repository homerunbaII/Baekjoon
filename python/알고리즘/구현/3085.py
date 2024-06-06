n = int(input())
arr = []
color = ['C','P','Z','Y']

for _ in range(n):
    arr.append(list(input()))

def check_arr(arr):
    maxi = 1
    for i in range(n):
        cnt = 1
        for j in range(n-1):
            if arr[i][j] == arr[i][j + 1]:
                cnt += 1
                maxi = max(maxi, cnt)
            else:
                cnt = 1
    for j in range(n):
        cnt = 1
        for i in range(n-1):
            if arr[i][j] == arr[i + 1][j]:
                cnt += 1
                maxi = max(maxi, cnt)
            else:
                cnt = 1
    return maxi

maxi = check_arr(arr)

for i in range(n):
    for j in range(n-1):
        if arr[i][j] != arr[i][j + 1]:
            temp_arr = [a[:] for a in arr]
            temp_arr[i][j], temp_arr[i][j+1] = arr[i][j + 1], arr[i][j]
            maxi = max(check_arr(temp_arr), maxi)

for j in range(n):
    for i in range(n-1):
        if arr[i][j] != arr[i + 1][j]:
            temp_arr = [a[:] for a in arr]
            temp_arr[i + 1][j], temp_arr[i][j] = arr[i][j], arr[i + 1][j]
            maxi = max(check_arr(temp_arr), maxi)

print(maxi)  