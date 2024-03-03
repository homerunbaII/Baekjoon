import sys

input = sys.stdin.readline

n , m = map(int, input().split())

n_list = []

for i in range(n):
    n_list.append(int(input()))

n_list.sort()


min_diff = 10e9
p1 = 0
p2 = 1
while p2 < n:
    diff = n_list[p2] - n_list[p1]
    if diff >= m :
        if diff < min_diff:
            min_diff = diff
        p1 += 1
        if p1 == p2:
            p2 = p1 + 1
    else:
        p2 += 1
    if min_diff == m :
        break


print(min_diff)
