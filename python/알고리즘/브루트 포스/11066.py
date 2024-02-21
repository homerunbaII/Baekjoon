from itertools import combinations, permutations

n = int(input())
power_list = [list(map(int, input().split())) for _ in range(n)]

# 각 팀원
team_person = n // 2
# 선수 번호 0 ~ n -1
player = [i for i in range(n)]
# 선수 번호는 0번부터 시작
team = list(combinations(range(1,n), team_person - 1))

# 팀 1
start_team = [[0] for _ in range(len(team))]
# 팀 2
link_team = []

for i in range(len(start_team)):
    start_team[i] = [0] + list(team[i])

# 팀 1, 팀 2 케이스 구하기

for i in start_team:
    temp = []
    for j in player:
        if j not in i:
            temp.append(j)
    link_team.append(temp)
            
start_team_power = []
link_team_power = []

# 각각 힘의 합 구하기

for i in start_team:
    power = 0
    temp = list(permutations(i, 2))
    for j in temp :
        x, y = j
        power += power_list[x][y]
    start_team_power.append(power)

for i in link_team:
    power = 0
    temp = list(permutations(i ,2))
    for j in temp :
        x, y = j
        power += power_list[x][y]
    link_team_power.append(power)

## 힘 차이 구하기
power_difference = []

for i in range(len(start_team_power)):
    power_difference.append(abs(start_team_power[i] - link_team_power[i]))

## 최소값 출력
print(min(power_difference))
    