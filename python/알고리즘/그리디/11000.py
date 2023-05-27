import sys
import heapq

heap = []
input = sys.stdin.readline

n = int(input())

arr = []
arr.append(list(map(int, input().split())))

arr.sort(key=lambda x: x[0])
heapq.heappush(heap, arr[0][1])
for i in range(n):
    if heap[0] > arr[i][0]:
        heapq.heappush[heap, arr[i][1]]
    else:
        heapq.heappop(heap)
        heapq.heappush[heap, arr[i][1]]
print(len(heap))
