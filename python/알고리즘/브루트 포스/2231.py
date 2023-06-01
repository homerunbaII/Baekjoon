n = int(input())
cnt = 0
flag = 0
k = n

for i in range(1, n + 1):
    temp = 0
    check = i
    if i < 10:
        pass
    else:
        temp = i
    while (i):
        temp += (i % 10)
        i //= 10
    if temp == n:
        flag = 1
        answer = check
        break

if flag == 1:
    print(answer)
else:
    print(0)
