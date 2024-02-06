
def dfs(cnt, arr):
    if cnt == m:
        ans.append(arr)
    for i in range(1, n + 1):
        if visited[i] == 0:
            visited[i] = 1
            dfs(cnt + 1, arr + [i])
            visited[i] = 0

n, m = map(int,input().split())

ans = []
visited = [0 for _ in range(n + 1)]
dfs(0, [])

for i in ans:
    print(*i)