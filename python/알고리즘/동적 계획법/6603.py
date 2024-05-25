def dfs(start, cnt, lst):
    if cnt == 6:
        print(*lst)
        return
    else:
        for i in range(start, n ):
            dfs(i + 1, cnt + 1, lst + [lottery[i]])

            
while True:
    arr = list(map(int, input().split()))
    n = arr[0]
    if n == 0:
        break
    lottery = arr[1:]
    dfs(0 ,0,[])
    print()

