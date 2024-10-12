n = int(input())

liquid = list(map(int, input().split()))

p1 = 0
p2 = n - 1

small = 10e20
small_p1 = -1
small_p2 = -1

if liquid[p2] <= 0:
    print(liquid[p2 - 1], liquid[p2])
elif liquid[p1] >= 0:
    print(liquid[p1], liquid[p1 + 1])
else:
    while True:
        now = liquid[p1] + liquid[p2]
        # 새로운 최소값 및 위치 저장
        if small > abs(now):
            small = abs(now)
            small_p1 = p1
            small_p2 = p2
        # 둘 숫자가 같아지면
        if p1 + 1 == p2:
            break
        # 합이 0이라면
        if now == 0:
            break
        # 0보다 크면 양수 줄이기
        elif now > 0:
            p2 -= 1
        # 0보다 작으면 음수 줄이기
        else:
            p1 += 1

    print(liquid[small_p1], liquid[small_p2])