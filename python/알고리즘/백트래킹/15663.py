n , m = map(int, input().split())
num_list =list(map(int, input().split()))
num_list.sort()
visited = [0 for _ in range(n)]
ans = []

def dfs(cnt, lst):
    if cnt == m:
        if lst not in ans:
            ans.append(lst)
    else:
        before = 0
        for i in range(n):
                if visited[i] == 0 and num_list[i] != before:
                    visited[i] = 1
                    dfs(cnt + 1, lst + [num_list[i]])
                    visited[i] = 0
                    before = num_list[i]

dfs(0, [])

for i in ans:
    print(*i)

