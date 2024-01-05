import heapq

sensor = int(input())
center = int(input())
sensor_list = list(map(int,input().split()))

sensor_list.sort()



total = sensor_list[-1] - sensor_list[0]
h = []

for i in range(sensor - 1):
    difference = sensor_list[i + 1] - sensor_list[i]
    heapq.heappush(h, -difference)

except_cnt = 0

for i in range(center - 1):
    except_cnt += heapq.heappop(h) * (-1)

print(total - except_cnt)

