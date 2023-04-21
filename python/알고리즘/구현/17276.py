import copy
import sys

input = sys.stdin.readline

t = int(input())


def rotate_45(arr, new_arr):
    for j in range(n):
        new_arr[j][j] = arr[(n-1)//2][j]
        new_arr[j][(n-1)//2] = arr[j][j]
        new_arr[j][n-1-j] = arr[j][(n-1)//2]
        new_arr[(n-1)//2][n-1 - j] = arr[j][n-1-j]


def rotate_R45(arr, new_arr):
    for j in range(n):
        new_arr[j][j] = arr[j][(n-1)//2]
        new_arr[j][(n-1)//2] = arr[j][n-1-j]
        new_arr[j][n-1-j] = arr[(n-1)//2][n-1-j]
        new_arr[(n-1)//2][n-1 - j] = arr[n-1-j][n-1-j]


for i in range(t):
    n, d = map(int, input().split())
    arr = []
    repeat = d // 45
    for j in range(n):
        arr.append(list(map(int, input().split())))
    new_arr = copy.deepcopy(arr)
    if d > 0:
        for _ in range(repeat):
            rotate_45(arr, new_arr)
            arr = copy.deepcopy(new_arr)
    if d < 0:
        for _ in range(abs(repeat)):
            rotate_R45(arr, new_arr)
            arr = copy.deepcopy(new_arr)
    for k in new_arr:
        print(*k)
