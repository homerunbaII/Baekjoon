a, b = map(int, input().split())
cnt = 0

while (b != a):
    temp = b
    cnt += 1
    if b % 2 == 0:
        b //= 2
    elif b % 10 == 1:
        b //= 10
    if temp == b:
        cnt = -1
        print(999)
        break


if cnt == -1:
    print(cnt)
else:
    print(cnt + 1)
