# N 극은 0 , S 극은 1
# 12시 방향부터 톱니바퀴의 방향이 주어진다
from collections import deque

### 비교할 덱리스트 넘버
### 톱니 1[2] 와 톱니2의 [6]
### 톱니 2[2] 와 톱니3의 [6]
### 톱니 3[2] 와 톱니4의 [6]


saw_1 = deque(map(int,input()))
saw_2 = deque(map(int,input()))
saw_3 = deque(map(int,input()))
saw_4 = deque(map(int,input()))


t = int(input())

for i in range(t):
    saw_num, rotate_direction = map(int, input().split())
    saw_status = [int(saw_1[2] != saw_2[6]), int(saw_2[2] != saw_3[6]), int(saw_3[2] != saw_4[6]) ]
    # 톱니 시작번호 1
    if saw_num == 1:
        # 1번 회전
        saw_1.rotate(rotate_direction)
        # 1,2가 다르다면
        if saw_status[0] == 1:
            saw_2.rotate(-rotate_direction)
            # 2,3이 다르다면
            if saw_status[1] == 1:
                saw_3.rotate(rotate_direction)
                # 3,4가 다르다면
                if saw_status[2] == 1:
                    saw_4.rotate(-rotate_direction)
    # 톱니 시작번호 2
    if saw_num == 2:
        # 2번 회전
        saw_2.rotate(rotate_direction)
        # 1,2, 다르다면 회전
        if saw_status[0] == 1:
            saw_1.rotate(-rotate_direction)
        # 2,3이 다르다면   
        if saw_status[1] == 1:
            saw_3.rotate(-rotate_direction)
                # 3,4가 다르다면
            if saw_status[2] == 1:
                    saw_4.rotate(rotate_direction)
    # 톱니 시작번호 3
    if saw_num == 3:
        saw_3.rotate(rotate_direction)
        # 1,2, 다르다면 회전
        if saw_status[2] == 1:
            saw_4.rotate(-rotate_direction)
        # 2,3이 다르다면   
        if saw_status[1] == 1:
            saw_2.rotate(-rotate_direction)
                # 3,4가 다르다면
            if saw_status[0] == 1:
                    saw_1.rotate(rotate_direction)
    # 톱니 시작번호 4
    if saw_num == 4:
        saw_4.rotate(rotate_direction)
        # 1,2가 다르다면
        if saw_status[2] == 1:
            saw_3.rotate(-rotate_direction)
            # 2,3이 다르다면
            if saw_status[1] == 1:
                saw_2.rotate(rotate_direction)
                # 3,4가 다르다면
                if saw_status[0] == 1:
                    saw_1.rotate(-rotate_direction)

print(saw_1[0] + 2 * saw_2[0] + 4 * saw_3[0] + 8 * saw_4[0] )





