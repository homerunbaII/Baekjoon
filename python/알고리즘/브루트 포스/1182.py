from itertools import combinations
n, total = map(int, input().split())
numbers = list(map(int, input().split()))
comb_list = []
cnt = 0
for i in range(1, n + 1):
    comb_list.append(list(combinations(numbers, i)))
print(comb_list)

for i in comb_list:
    for j in range(len(i)):
        if sum(i[j]) == total:
            cnt += 1
print(cnt)