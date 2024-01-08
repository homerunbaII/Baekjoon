import sys , heapq

n = int(input())
h = []
for i in range(n):
    card = int(input())
    heapq.heappush(h,card )

count = 0
print(h)
while len(h) > 1:
    small_1 =heapq.heappop(h)
    small_2 =heapq.heappop(h)
    new = small_1 + small_2
    heapq.heappush(h ,new)
    count += new

print(count)