n , m =map(int, input().split())
num_list = list(map(int, input().split()))
num_list = list(set(num_list))
num_list.sort()

ans = []

def dfs(cnt, lst, before):
    if cnt == m:
        ans.append(lst)
    else:
        for i in num_list:
            if i >= before:
                before = i
                dfs(cnt + 1, lst + [i], before)

dfs(0, [], 0)

for i in ans:
    print(*i)