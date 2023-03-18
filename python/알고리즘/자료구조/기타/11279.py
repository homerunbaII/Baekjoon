# from queue import PriorityQueue

# n = int(input())

# que = PriorityQueue(maxsize=100000)

# for i in range(n):
#     x = int(input())
#     if x == 0:
#         if que.empty() == True:
#             print(0)
#         else:
#             print(que.get()[1])
#     else:
#         x_sort = (-x, x)
#         que.put(x_sort)]
import sys
from heapq import *

heap = []

n = int(input())

for i in range(n):
    x = int(sys.stdin.readline())
    if x == 0:
        if heap:
            print(-heappop(heap))
        else:
            print(0)
    else:
        heappush(heap, -x)
