# up = []
# down = []
# key_list = []


# w, l, n = map(int, input().split())

# unique_key = n

# for i in range(n):
#     up.append([*map(int, input().split())])
#     down.append([*map(int, input().split())])

# for i in range(n):
#     key_list.append([[], []])
#     for j in range(l):
#         key_list[i][0].append(w - (up[i][j] + down[i][j]))  # 열쇠의 높이
#     for k in range(l-1):
#         key_list[i][1].append(up[i][k] - up[i][k+1])  # 한 구간과 다음 구간의 차이


# for i in range(n - 1):
#     check_same = 0
#     for j in range(i + 1, n):  # 열쇠의 높이와 구간차 비교
#         print(i, j, '번째와 비교')
#         # 만약에 높이와 구간차가 같다면, 같은 열쇠이다
#         if key_list[i][0] == key_list[j][0] and key_list[i][1] == key_list[j][1]:
#             check_same += 1
#     print(check_same, 'checksame')
#     if check_same > 0:
#         unique_key -= 1


# print(unique_key)

w, l, n = map(int, input().split())
up = []
down = []
key_list = []
unique_key = n

for i in range(n):
    up.append([*map(int, input().split())])
    down.append([*map(int, input().split())])

for i in range(n):
    key_list.append([[], [], []])
    for j in range(l):
        key_list[i][0].append(w - (up[i][j] + down[i][j]))  # 열쇠의 높이
    for k in range(l-1):
        key_list[i][1].append(up[i][k] - up[i][k+1])  # 한 구간과 다음 구간의 차이
        key_list[i][1].append(up[i][k] - up[i][k+1])

for i in range(n - 1):
    check_same = 0
    for j in range(i + 1, n):  # 열쇠의 높이와 구간차 비교
        # 만약에 높이와 구간차가 같다면, 같은 열쇠이다
        print(key_list[i][0], key_list[j][0], key_list[i][1], key_list[j][1])
        if key_list[i][0] == key_list[j][0] and key_list[i][1] == key_list[j][1]:
            check_same += 1
        if key_list[i][0][::-1] == key_list[j][0] and key_list[i][1] == key_list[j][1][::-1]:
            check_same += 1
    if check_same > 0:
        unique_key -= 1


print(unique_key)
