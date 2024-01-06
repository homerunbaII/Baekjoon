import sys

input = sys.stdin.readline

crane = int(input())
crane_weight_limit = list(map(int,input().split()))

box = int(input())
box_weight = list(map(int,input().split()))

crane_weight_limit.sort(reverse= True)

box_weight.sort(reverse= True)

time = 0

if box_weight[0] > crane_weight_limit[0]:
    print(-1)
    sys.exit()

while box_weight:
    for crane in crane_weight_limit:
        for box in box_weight:
            if crane >= box:
                box_weight.remove(box)
                break
    time += 1

print(time)






