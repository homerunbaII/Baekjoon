import sys
from itertools import permutations

input = sys.stdin.readline

def find_score(order, n, result):
    score = 0
    p = 0  # 타자 순서
    for inning in range(n):
        out_count = 0
        base = [0, 0, 0]
        while out_count < 3:
            player_now = order[p] - 1
            record = result[inning][player_now]
            if record == 0:
                out_count += 1
            elif record == 4:
                score += 1 + sum(base)
                base = [0, 0, 0]
            else:
                for i in range(2, -1, -1):
                    if base[i] == 1:
                        if i + record >= 3:
                            score += 1
                        else:
                            base[i + record] = 1
                        base[i] = 0
                base[record - 1] = 1
            p = (p + 1) % 9

    return score

# 이닝
n = int(input())

result = [list(map(int, input().split())) for _ in range(n)]

max_score = 0

fixed_order = [1] * 9
for i, perm in enumerate(permutations(range(2, 10), 8), start=1):
    order = list(perm[:3]) + [1] + list(perm[3:])
    max_score = max(max_score, find_score(order, n, result))

print(max_score)