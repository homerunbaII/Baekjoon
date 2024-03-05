n, m = map(int, input().split())
set_6 = []
ind = []

for _ in range(m):
    a, b = map(int, input().split())
    set_6.append(a)
    ind.append(b)

# 가장 저렴한 세트와 낱개 가격을 찾습니다.
set_6.sort()
ind.sort()

# 세트로만 구매하는 경우와 남은 개수를 낱개로 구매하는 경우의 비용
cost_with_set = set_6[0] * (n // 6) + ind[0] * (n % 6)
# 모두 세트로 구매하는 경우 (남은 개수가 있더라도 추가 세트 구매가 더 저렴할 수 있음)
cost_all_set = set_6[0] * ((n + 5) // 6)
# 모두 낱개로 구매하는 경우
cost_all_individual = ind[0] * n

# 최소 비용 계산
answer = min(cost_with_set, cost_all_set, cost_all_individual)

print(answer)