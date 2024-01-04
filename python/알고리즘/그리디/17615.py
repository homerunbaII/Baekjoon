n = int(input())
ball_order = input()

R_cnt_1 = 0
B_cnt_1 = 0


stop = n - 1

## case 1
while stop > 0:
    if ball_order[stop] == ball_order[stop - 1]:
        stop -= 1
        if stop == 1:
            break
    else:
        stop -= 1
        break


for i in range(stop, -1,-1):
    if ball_order[i] == 'R':
        R_cnt_1 += 1
    if ball_order[i] == 'B':
        B_cnt_1 += 1

## case 2
stop = 0
R_cnt_2 = 0
B_cnt_2 = 0

while stop < n - 1:
    if ball_order[stop] == ball_order[stop + 1]:
        stop += 1
    else:
        stop += 1
        break

for i in range(stop, n, 1):
    if ball_order[i] == 'R':
        R_cnt_2 += 1
    if ball_order[i] == 'B':
        B_cnt_2 += 1



print(min(B_cnt_1,B_cnt_2,R_cnt_1,R_cnt_2))