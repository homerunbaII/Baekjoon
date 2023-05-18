n = int(input())
br_list = list(input())
b_cnt = 0
r_cnt = 0
cnt = 0

for i in range(n):
    if i == 0:
        continue
    if br_list[0] == 'B':
        if br_list[i - 1] == 'B' and br_list[i] == 'R':
            cnt += 1
    if br_list[0] == 'R':
        if br_list[i - 1] == 'R' and br_list[i] == 'B':
            cnt += 1

print(cnt + 1)
