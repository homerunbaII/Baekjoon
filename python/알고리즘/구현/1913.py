n = int(input())

arr = [[0 for _ in range(n)] for _ in range(n)]

target = int(input())  # 5칸 밑으로 7칸 오른쪽으로 -> 배열로 표기하면 arr[4][6]

i = 0
j = 0
start = n ** 2
repeat = n - 1
cnt = 0
cnt2 = 0

while (start):
    if start == target:
        target_x, target_y = i, j
    arr[i][j] = start
    start -= 1
    if cnt == 0:
        i += 1
        if repeat == 1:
            cnt = 1
            repeat = n - 1 - cnt2
            continue
    elif cnt == 1:
        j += 1
        if repeat == 1:
            cnt = 2
            repeat = n - 1 - cnt2
            continue
    elif cnt == 2:
        i -= 1
        if repeat == 1:
            cnt = 3
            repeat = n - 1 - cnt2
            continue
    elif cnt == 3:
        j -= 1
        if repeat == 1:
            j += 1
            i += 1
            cnt = 0
            cnt2 += 2
            repeat = n - 1 - cnt2
            continue
    repeat -= 1


for i in range(n):
    print(*arr[i])
print(target_x + 1, target_y + 1)
