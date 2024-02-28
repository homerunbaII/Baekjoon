import sys

n = int(input())

n_list = list(map(int, input().split()))

n_list.sort()

plus = 0
minus = 0

# 음수만 존재
for i in n_list:
    # 양수라면
    if i >= 0:
        plus = 1
        break

# 양수만 존재
for i in n_list:
    if i <= 0:
        minus = 1
        break

small = [sys.maxsize, 0, 0]
result = []

if plus == 1 and minus == 1:
    p1 = 0
    p2 = n -1 
    # 이게 양수면 양수쪽 -1
    p2 - p1
    # 이게 음수면 음수쪽 + 1
    while True:
        if p1 == p2:
            break
        diff = n_list[p2] + n_list[p1]
        if abs(diff) < small[0]:
            small = [abs(diff), n_list[p1], n_list[p2]]
        else:
            pass
        # 양수 쪽이 크다면
        if diff > 0:
            p2 -= 1
        # 음수 쪽이 크다면
        elif diff < 0:
            p1 += 1
        # 차이가 0이라면
        else:
            small = [0, n_list[p1], n_list[p2]]
            break
    print(small[1], small[2])
# 양수 & 0
elif plus == 1 and minus == 0:
    print(n_list[0] , n_list[1])
# 음수 & 0
elif minus == 1 and plus == 0:
    print(n_list)
    print(n_list[-2] , n_list[-1])

