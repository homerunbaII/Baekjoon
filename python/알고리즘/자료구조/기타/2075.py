import sys
import heapq

n = int(input())

heap = []

for _ in range(n):
    temp = list(map(int, sys.stdin.readline().split()))
    for i in temp:
        if len(heap) < n:
            heapq.heappush(heap, i)
        else:
            if heap[0] < i:
                heapq.heappop(heap)
                heapq.heappush(heap, i)
            else:
                pass

print(heap[0])
