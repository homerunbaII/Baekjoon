from collections import deque

# 트럭 수 , 다리 길이, 다리 하중
n , l, w = map(int, input().split())

truck_order = deque(list(map(int, input().split())))

bridge = deque([0 for _ in range(l)])
time = 0
#[0,0,3]
while truck_order:
    time += 1
    bridge.popleft()
    bridge.append(0)
    # 다음 들어올 트럭의 무게와 현재 다리에 있는 무게의 합 <= 다리 하중
    if sum(bridge) + truck_order[0] <= w:
        bridge[-1] = truck_order.popleft()

time += len(bridge)

print(time)

