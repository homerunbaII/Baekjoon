n = int(input())

cnt = 0 
check = 0
while True:
    if n == 8:
        cnt += 4
        break
    if n == 6:
        cnt += 3
        break
    if n == 4:
        cnt += 2
        break
    if n == 2:
        cnt += 1
        break
    if n == 0:
        cnt += 0
        break
    n -= 5
    cnt += 1
    if cnt > 50000:
        check = 1
        break

if check == 0:
    print(cnt)
else:
    print(-1)
