import sys
input = sys.stdin.readline

day, trial = map(int,input().split())
plan = [int(input()) for _ in range(day)]


start = max(plan)
end = sum(plan)

while start <= end:
    mid = (start + end) // 2
    budget = mid
    cnt = 1
    for i in plan:
        if budget < i:
            # 반납 후 인출
            budget = mid
            # 인출 횟수
            cnt += 1
        # 차감
        budget -= i
    if cnt > trial :
        start = mid + 1
    else:
        end = mid - 1
print(start)

