n, m  = map(int, input().split())

visited = [0 for _ in range(n + 1)]
ans = []

def dfs(cnt, lst):
    if cnt == m:
        lst.sort()
        if lst not in ans:
            ans.append(lst)
    else:    
        for i in range(1, n + 1):
            if visited[i] == 0:
                visited[i] = 1
                dfs(cnt + 1, lst + [i])
                visited[i] = 0

dfs(0, [])

for i in ans:
    print(*i)