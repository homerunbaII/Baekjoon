t = int(input())

for i in range(t):
    n = int(input())
    r = n % 5
    n = n - r
    cnt_5 = 5
    cnt = 0
    while cnt_5 <= n:
        cnt += int(n / cnt_5)
        cnt_5 *= 5
    print(cnt)
