n , m = map(int, input().split())
num_list = list(map(int, input().split()))
num_list.sort()

ans = []

def dfs(cnt, lst, before):
    if cnt == m:
        ans.append(lst)
    else:
        for i in num_list:
            if i >= before:
                dfs(cnt + 1, lst + [i], i)

dfs(0, [], num_list[0])

for i in ans:
    print(*i)
