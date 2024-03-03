import heapq

n = int(input())

maybe_rank = []
real_rank = [0 for _ in range(n)]

for i in range(n):
    rank = int(input())
    if rank > n:
        heapq.heappush(maybe_rank, rank)
    else:
        if real_rank[rank - 1] == 0:
            real_rank[rank - 1] = rank
        else:
            heapq.heappush(maybe_rank, rank)
mad = 0

i = 0
while i < n:
    if real_rank[i] == 0:
        a = heapq.heappop(maybe_rank)
        real_rank[i] = a
        mad += abs((i + 1) - a)
    i += 1
print(mad)