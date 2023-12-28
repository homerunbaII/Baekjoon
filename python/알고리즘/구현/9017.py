t = int(input())

for i in range(t):
    n = int(input())
    rank_list = list(map(int, input().split()))
    real_teams = []
    for j in range(1,201):
        checker = 0
        for k in rank_list:
            if j == k :
                checker += 1
        if checker < 6:
            while j in rank_list:
                rank_list.remove(j)
        else:
            real_teams.append(j)
    winner_list = []
    for j in real_teams:
        player_cnt = 0
        team_score_tmp = 0
        for k in range(len(rank_list)):
            if j == rank_list[k]:
                player_cnt +=1
                if player_cnt < 5:
                    team_score_tmp += (k + 1)
                if player_cnt == 4:
                    team_score = team_score_tmp
                if player_cnt == 5:
                    winner_list.append([j,team_score,k + 1])
                    break
    team = sorted(winner_list, key=lambda x:(x[1], x[2]))
    print(team[0][0])