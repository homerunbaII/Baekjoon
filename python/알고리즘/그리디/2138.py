def change_state(light_state,now, n):
        if now != n - 1:
            for i in range(3):
                light_state[now + i - 1] = 1 - light_state[now + i - 1] 
        else:    
            for i in range(2):
                light_state[now + i - 1] = 1 - light_state[now + i - 1] 

n = int(input())

original_light = list(map(int, str(input())))
target_light = list(map(int, str(input())))

# case 1
case_1 = list(original_light)
cnt_case_1 = 0


for i in range(1, n):
    if case_1[i - 1] != target_light[i - 1]:
        change_state(case_1, i, n)
        cnt_case_1 += 1
    else:
        pass


for i in range(n):
    if case_1[i] != target_light[i]:
        cnt_case_1 = -1
        break

# case 2
case_2 = list(original_light)
cnt_case_2 = 1

case_2[0] = 1 - case_2[0]
case_2[1] = 1 - case_2[1]

for i in range(1, n):
    if case_2[i - 1] != target_light[i - 1]:
        change_state(case_2, i, n)
        cnt_case_2 += 1
    else:
        pass



for i in range(n):
    if case_2[i] != target_light[i]:
        cnt_case_2 = -1
        break

if cnt_case_1 == -1 and cnt_case_2 == -1:
    print(-1)
elif cnt_case_1 == -1 and cnt_case_2 != -1:
    print(cnt_case_2)
elif cnt_case_1 != -1 and cnt_case_2 == -1:
    print(cnt_case_1)
elif cnt_case_1 < cnt_case_2:
    print(cnt_case_1)
else:
    print(cnt_case_2)   
