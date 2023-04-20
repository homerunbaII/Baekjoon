t = int(input())


def rotate_45(arr):
    for j in range(n):
        arr[j][(n+1)//2-1], arr[j][n-1-j], arr[(n+1)//2 -
                                               1][j], arr[j][j] = arr[j][j], arr[j][(n+1)//2-1], arr[j][n-1-j], arr[(n+1)//2-1][j]
    return arr


def rotate_M45(arr):

    pass


for i in range(t):
    n, d = map(int, input().split())
    arr = []
    repeat = d // 45
    for i in range(n):
        arr.append(list(map(int, input().split())))
        pass
    if repeat > 0:
        for _ in range(repeat):
            arr = list(rotate_45(arr))
    if d == -45:
        pass

print(arr)
# temp1.append(arr[j][j])
# temp2.append(arr[j][(n+1)//2-1])
# temp3.append(arr[j][n-1-j])
# temp4.append(arr[(n+1)//2-1][j])
