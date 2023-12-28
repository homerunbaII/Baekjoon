n = int(input())

time_std = 0
team_1_win_time = 0
team_2_win_time = 0
team_1_score = 0
team_2_score = 0
winning_team = 0

for i in range(n + 1):
    if i < n:
        team_num, time = input().split()
        team_num = int(team_num)
        time_min, time_sec = int(time[0:2]), int(time[3:5])
        total_sec = 60 * time_min + time_sec
        
        team_win_time = total_sec - time_std
        time_std = total_sec
    elif i == n:
        team_win_time = (48 * 60) - time_std

    if winning_team == 1:
        team_1_win_time += team_win_time
    elif winning_team == 2:
        team_2_win_time += team_win_time
    else:
        pass
        
    if team_num == 1:
        team_1_score += 1
    else:
        team_2_score += 1
    
    if team_1_score > team_2_score:
        winning_team = 1
    elif team_2_score > team_1_score:
        winning_team = 2
    else:
        winning_team = 0
    
    
        

team_1_min, team_1_sec = team_1_win_time // 60 ,team_1_win_time % 60
team_2_min, team_2_sec = team_2_win_time // 60 , team_2_win_time % 60

team1_total = print(f'{team_1_min:02d}:{team_1_sec:02d}') 
team2_total = print(f'{team_2_min:02d}:{team_2_sec:02d}') 
