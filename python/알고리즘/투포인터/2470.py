import sys

n = int(input())

n_list = list(map(int, input().split()))

n_list.sort()

small = [sys.maxsize, 0, 0]

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
