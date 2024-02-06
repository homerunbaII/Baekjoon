n, m  = map(int, input().split())

visited = [0 for _ in range(n + 1)]
ans = []

def dfs(cnt, lst, last):
    if cnt == m:
        ans.append(lst)
    else:    
        for i in range(last, n + 1):
            if visited[i] == 0:
                visited[i] = 1
                dfs(cnt + 1, lst + [i], i)
                visited[i] = 0

dfs(0, [], 1)

for i in ans:
    print(*i)