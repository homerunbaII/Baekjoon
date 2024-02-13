n = int(input())
# < > < >
operation = list(input().split())
# 0 1 2 3 4 5 6 7 8 9
visited = [0 for _ in range(10)]
result = []

def dfs(cnt,lst, before):
    if cnt == n + 1:
        lst = list(map(str, lst))
        lst = ''.join(lst)
        result.append(lst)
    else:
        if cnt == 0:
                for i in range(0, 10):
                    visited[i] = 1
                    dfs(cnt + 1,lst + [i], i)
                    visited[i] = 0
        else:
            for i in range(0, 10):
                if visited[i] == 0:
                    if operation[cnt - 1] == '>': 
                        if before > i:
                            visited[i] = 1
                            dfs(cnt + 1,lst + [i], i)
                            visited[i] = 0 
                    elif operation[cnt - 1] == '<':
                        if before < i:
                            visited[i] = 1
                            dfs(cnt + 1,lst + [i], i)
                            visited[i] = 0
                    

dfs(0,[],0)

print(max(result))
print(min(result))