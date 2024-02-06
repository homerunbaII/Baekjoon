n, m = map(int, input().split())
ans = []

def dfs(cnt, lst, end):
    if cnt == m:
        ans.append(lst)
    else:
        for i in range(end, n + 1):
            dfs(cnt + 1, lst + [i], i)
            

dfs(0,[],1)
print(ans)