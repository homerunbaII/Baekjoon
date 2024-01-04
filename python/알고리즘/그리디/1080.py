def change3_3(list, start_list_num, start_index_num):
    for i in range(3):
        for j in range(3):
            list[start_list_num + i][start_index_num + j] = 1 - list[start_list_num + i][start_index_num + j]

n, m = map(int,input().split())

origin_list = []
changed_list = []

trial = 0
checker = 0

for _ in range(n):
    origin_list.append(list(map(int, input())))

for _ in range(n):
    changed_list.append(list(map(int, input())))

for i in range(n - 2):
    for j in range(m - 2):
        if origin_list[i][j] != changed_list[i][j]:
            change3_3(origin_list, i , j)
            trial += 1

for i in range(n ):
    for j in range(m):
        if origin_list[i][j] != changed_list[i][j]:
            trial = -1

print(trial)



