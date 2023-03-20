import heapq
import sys

heap_plus = []

heap_minus = []

n = int(input())

for i in range(n):
    x = int(sys.stdin.readline())
    if x == 0:
        if heap_minus and heap_plus:
            if abs(heap_minus[0]) > abs(heap_plus[0]):
                print(heapq.heappop(heap_plus))
            elif abs(heap_minus[0]) < abs(heap_plus[0]):
                print(-heapq.heappop(heap_minus))
            elif abs(heap_minus[0]) == abs(heap_plus[0]):
                print(-heapq.heappop(heap_minus))
        elif heap_plus and not heap_minus:
            print(heapq.heappop(heap_plus))
        elif heap_minus and not heap_plus:
            print(-heapq.heappop(heap_minus))
        else:
            print(0)
    if x > 0:
        heapq.heappush(heap_plus, x)
    if x < 0:
        heapq.heappush(heap_minus, -x)


# import sys
# import heapq

# n = int(input())
# q = []

# for i in range(n):
#     a = int(sys.stdin.readline().rstrip())
#     if a != 0:
#         heapq.heappush(q, (abs(a), a))
#     else:
#         if not q:
#             print(0)
#         else:
#             print(heapq.heappop(q)[1])
