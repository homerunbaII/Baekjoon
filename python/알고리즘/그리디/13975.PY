import sys, heapq
input = sys.stdin.readline

t = int(input())

for i in range(t):
    chapter = int(input())
    chapter_list = list(map(int, input().split()))
    cost = 0
    h = []
    for i in chapter_list:
        heapq.heappush(h,i)
    chapter_list.sort()
    while len(h) != 1:
        small_1 = heapq.heappop(h)
        small_2 = heapq.heappop(h)
        new = small_1 + small_2
        cost += new
        heapq.heappush(h ,new)
    print(cost)

