import sys

input = sys.stdin.readline

n, k = map(int, input().split())
s = list(map(int, input().split()))

check = k
cnt = 0


for i in range(n):
    j = 0
    while (check >= 0 and i + j < n):
        if s[i + j] % 2 == 1:
            cnt += 1
        else:
            check -= 1
        j += 1
    s[i] = cnt
    cnt = 0
    check = k


print(max(s))
