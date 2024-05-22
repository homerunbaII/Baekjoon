n, k = map(int, input().split())

arr = [i for i in range(1, n + 1)]
ans = []

pnt = 0
cnt = n
check = 0

while cnt:
    if arr[pnt] == 0:
        pnt += 1
        pnt %= n
        continue
    else:
        if check == k - 1:
            ans.append(arr[pnt])
            arr[pnt] = 0
            cnt -= 1
            check = 0    
        else:
            check += 1
            pnt += 1
            pnt %= n


print(f"<{', '.join(map(str, ans))}>")



    




