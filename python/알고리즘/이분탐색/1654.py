import sys

input = sys.stdin.readline

n, need = map(int, input().split())
lan_list = [int(input()) for  _ in range(n)]


start = 1
end = max(lan_list)

while start <= end:
    cnt = 0
    mid = (start + end) // 2
    for i in lan_list:
        cnt += (i // mid)
    if cnt >= need :
        start = mid + 1
    else:
        end = mid - 1
print(end)