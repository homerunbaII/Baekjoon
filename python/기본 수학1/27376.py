# n미터
# 신호등 k개
# i = 1번째 신호등 ti초 동안 번갈아 켜짐
# 주행시점 si초 후에 빨~초
# mobis의 속도는 1m/s

n, k = map(int, input().split())  # 미터, 신호등 입력받는다

traffic_light_list = []
sec = 0

for i in range(k):
    traffic_light_list.append(
        list(map(int, input().split())))  # 신호등의 리스트를 입력받는다

traffic_light_list.sort(key=lambda x: x[0])  # 신호등 위치를 기준으로 오름차순 정렬한다
traffic_light_distance_list = []

for p1, p2 in zip(traffic_light_list, traffic_light_list[1:]):
    distance = p2[0] - p1[0]  # 신호등 간의 거리 리스트를 생성한다
    traffic_light_distance_list.append(distance)

# 처음 시작점 0 부터 첫번째 신호등까지의 거리를 append해준다
traffic_light_distance_list.insert(0, traffic_light_list[0][0])

j = 0

for i in traffic_light_list:
    sec += traffic_light_distance_list[j]  # 신호등간의 거리를 sec 에 더해준다
    j += 1
    location = i[0]
    frequency = i[1]
    start = i[2]
    if (start > sec):  # 신호등의 켜지는 시간이 자동차가 도착한 시간보다 느리다면 그 시간이 통과시간
        sec = start
    if (0 < (sec - start + 1) % (frequency * 2) < frequency):  # 초록불일 때 다음 신호등으로 통과
        continue
    sec += (frequency * 2) - (sec - start + 1) % (frequency * 2) + \
        1  # 빨간불일 때 신호등이 초록불일 때까지 대기하는 시간

sec += n - i[0]  # 마지막 신호등에서 도착점까지의 거리를 더해준다
print(sec)
