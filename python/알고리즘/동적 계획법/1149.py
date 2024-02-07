import sys
input = sys.stdin.readline

n = int(input())
rgb = [0 for _ in range(n)]

for i in range(n):
    rgb[i] = list(map(int,input().split()))

for i in range(1 , n):
    rgb[i][0] += min(rgb[i-1][1], rgb[i-1][2])
    rgb[i][1] += min(rgb[i-1][0], rgb[i-1][2] )
    rgb[i][2] += min(rgb[i-1][0], rgb[i-1][1] )

print()

print(min(rgb[n - 1]))