import sys, heapq

n = int(sys.stdin.readline())

cnt = 1
meeting_list = []

for i in range(n):
    start, end = map(int, sys.stdin.readline().rstrip().split())
    meeting_list.append([start,end])

meeting_list.sort(key = lambda x : x[0])

heap = [0]

for start, end in meeting_list:
    if start >= heap[0]:
        heapq.heappop(heap)
    else:
        cnt += 1
    heapq.heappush(heap, end)

print(cnt)
