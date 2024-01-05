import heapq

n, group = map(int,input().split())
kid_list = list(map(int,input().split()))

total = kid_list[-1] - kid_list[0]

h = []


for i in range(n - 1):
    difference = kid_list[i+1] - kid_list[i]
    heapq.heappush(h, -difference)

except_cnt = 0

for i in range(group - 1):
    except_cnt += heapq.heappop(h) * - 1

print(total - except_cnt)