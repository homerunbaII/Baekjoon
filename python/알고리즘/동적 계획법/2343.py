total, target = map(int, input().split())
lec_list = list(map(int, input().split()))

start = min(lec_list)
end = sum(lec_list)

while start <= end:
    mid = (start + end) // 2
    cnt = 1
    length = 0
    for i in lec_list:
        if length + i > mid:
            length = 0
            length += i
            cnt += 1
        else:
            length += i
    if cnt > target:
        start = mid + 1
    else:
        end = mid -1


print(start)