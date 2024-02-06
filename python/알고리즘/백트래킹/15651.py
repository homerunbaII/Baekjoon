n , m  = map(int, input().split())

ans = []
visited = [0 for _ in range(n + 1)]

def dfs(cnt, lst):
    if cnt == m:
        ans.append(lst)
    else:
        for i in range(1, n + 1):
            dfs(cnt + 1, lst + [i])

dfs(0, [])

for i in ans:
    print(*i)