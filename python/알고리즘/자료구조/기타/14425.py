import sys

input = sys.stdin.readline

n, m = map(int, input().split())
cnt = 0
s = {}

for _ in range(n):
    x = input().rstrip()
    s[x] = True

for j in range(m):
    a = input().rstrip()
    if a in s:
        cnt += 1

print(cnt)
