import heapq

n, m = map(int, input().split())

temp = list(map(int, input().split()))

card_list = []

for i in temp:
    heapq.heappush(card_list, i)

while m:
    small_1 = heapq.heappop(card_list)
    small_2 = heapq.heappop(card_list)
    total = small_1 + small_2
    
    heapq.heappush(card_list, total)
    heapq.heappush(card_list, total)
    
    m -= 1

print(sum(card_list))