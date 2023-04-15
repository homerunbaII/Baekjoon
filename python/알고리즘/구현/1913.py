n = int(input())

arr = [[0 for _ in range(n)] for _ in range(n)]

y, x = map(int, input().split())  # 5칸 밑으로 7칸 오른쪽으로 -> 배열로 표기하면 arr[4][6]

i = 0
j = 0
start = n ** 2
repeat = n - 1
cnt = 0
cnt2 = 0

while (start):
    arr[i][j] = start
    print('i', i, 'j', j, 'cnt', cnt, 'start', start)
    print('repeat', repeat)
    start -= 1
    if cnt == 0:
        i += 1
        repeat -= 1
        if repeat == 0:
            cnt = 1
            repeat = n - 1 - cnt2
            continue
    elif cnt == 1:
        j += 1
        repeat -= 1
        if repeat == 0:
            cnt = 2
            repeat = n - 1 - cnt2
            continue
    elif cnt == 2:
        repeat -= 1
        i -= 1
        if repeat == 0:
            cnt = 3
            repeat = n - 1 - cnt2
            continue
    elif cnt == 3:
        repeat -= 1
        j -= 1
        if repeat == 1:
            cnt = 0
            cnt2 += 2
            repeat = n - 1 - cnt2
            continue


print(arr)
