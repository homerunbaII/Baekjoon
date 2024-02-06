n, m = map(int, input().split())

num_list= list(map(int, input().split()))
num_list.sort()
max_num = max(num_list)
ans = []
visited = [0 for _ in range(max_num + 1)]

def dfs(cnt,lst):
    if cnt == m:
        ans.append(lst)
    else:
        for i in num_list:
            if visited[i] == 0:
                visited[i] = 1
                dfs(cnt + 1, lst + [i])
                visited[i] = 0
dfs(0, [])

for i in ans:
    print(*i)
