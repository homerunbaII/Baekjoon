n , lasts = map(int, input().split())

city = [list(map(int, input().split())) for _ in range(n)]
house_lc = []
chicken_lc =  []

for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            house_lc.append([i,j])
        if city[i][j] == 2:
            chicken_lc.append([i,j])

distance_list = [[]for _ in range(len(house_lc))]

for i in range(len(house_lc)):
    x,y = house_lc[i]
    for j in range(len(chicken_lc)):
        t_x , t_y = chicken_lc[j]
        distance = abs(x - t_x) + abs(y - t_y)
        distance_list[i].append(distance)

visited = [0 for _ in range(len(chicken_lc))]
house_ans = []
distance_check = [[] for _ in range(len(house_lc))]

#  last = 2개
def dfs(cnt, start, lst):
    ### [2,6], [2,2], [2,4], [5,3], [6,4], [6,4]
    if cnt == lasts:
        ans = 0
        for i in lst:
            ans += min(i)
        house_ans.append(ans)
    else : 
        for i in range(start, len(chicken_lc)):
            if visited[i] == 0:
                visited[i] = 1
                for j in range(len(distance_list)):
                    lst[j].append(distance_list[j][i])
                dfs(cnt + 1, i ,lst)
                visited[i] = 0
                for j in lst:
                    j.pop()

dfs(0, 0, distance_check)

print(min(house_ans))