belt_length, durability_max = map(int, input().split())
durability_list = list(map(int,input().split()))

for i in range(len(durability_list)):
    durability_list[i] = [0, durability_list[i]]



def checkdurablility(list):
    check = 0
    for i in list:
        if i[1] == 0:
            check += 1
    return check

stage = 0

while checkdurablility(durability_list) < durability_max:
    stage += 1
    durability_list.insert(0 ,durability_list.pop())
    if durability_list[belt_length][0] == 1:
        durability_list[belt_length][0] = 0
    if durability_list[belt_length - 1][0] == 1:
        durability_list[belt_length - 1][0] = 0
    for i in range(belt_length):
        ## 현재 벨트에 로봇이 있고 and 다음 벨트에 로봇이 없고 and 다음 벨트의 내구도가 남은 경우
        if durability_list[belt_length - 1 - i][0] == 1 and durability_list[belt_length - i][0] == 0 and durability_list[belt_length - i][1] > 0:
            durability_list[belt_length - 1 - i][0] = 0
            durability_list[belt_length - i][0]  = 1
            durability_list[belt_length - i][1] -= 1
    if durability_list[belt_length][0] == 1:
        durability_list[belt_length][0] = 0
    if durability_list[0][1] > 0:
        durability_list[0][0] = 1
        durability_list[0][1] -= 1
    
        

print(stage)



